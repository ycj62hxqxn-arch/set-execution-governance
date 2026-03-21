import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// --- CONTROL LAYERS ---

function parser(input) {
  return input.toLowerCase();
}

function ruleEngine(input) {
  if (input.includes("hack") || input.includes("fraud")) {
    return { allowed: false, reason: "High risk detected" };
  }
  return { allowed: true };
}

function authorityGate(ruleResult) {
  if (!ruleResult.allowed) {
    return { approved: false, message: "Blocked by governance layer" };
  }
  return { approved: true };
}

// --- ROUTE ---

app.post("/execute", async (req, res) => {
  const userInput = req.body.input;

  const parsed = parser(userInput);
  const rules = ruleEngine(parsed);
  const authority = authorityGate(rules);

  if (!authority.approved) {
    return res.json({
      status: "blocked",
      reason: rules.reason
    });
  }

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4.1-mini",
      messages: [
        { role: "system", content: "You are a controlled AI operating under governance rules." },
        { role: "user", content: userInput }
      ]
    });

    res.json({
      status: "approved",
      output: response.choices[0].message.content
    });

  } catch (err) {
    res.status(500).json({ error: "AI error" });
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});Approve payment
