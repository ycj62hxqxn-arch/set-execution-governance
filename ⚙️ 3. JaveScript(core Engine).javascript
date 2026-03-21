function logStep(text, className="") {
  const log = document.getElementById("log");
  const div = document.createElement("div");
  div.className = className;
  div.innerText = text;
  log.appendChild(div);
}

function clearLog() {
  document.getElementById("log").innerHTML = "";
}

function runAI() {
  clearLog();

  const input = document.getElementById("userInput").value.toLowerCase();

  // STEP 1: Parsing
  logStep("Parsing input...", "step");

  setTimeout(() => {
    
    // STEP 2: Logic
    logStep("Applying logic engine...", "step");

    setTimeout(() => {

      // STEP 3: Rules
      logStep("Evaluating rules...", "step");

      let risk = "low";

      if (input.includes("fraud") || input.includes("hack")) {
        risk = "high";
      }

      setTimeout(() => {

        // STEP 4: Authority Gate
        logStep("Authority Gate check (QGED)...", "step");

        setTimeout(() => {

          if (risk === "high") {
            logStep("❌ BLOCKED: Policy violation detected", "blocked");
          } else {
            logStep("✔ APPROVED: Execution allowed", "approved");
          }

        }, 800);

      }, 800);

    }, 800);

  }, 800);
}
function logStep(text, className="") {
  const log = document.getElementById("log");
  const div = document.createElement("div");
  div.className = className;
  div.innerText = text;
  log.appendChild(div);
}

function clearLog() {
  document.getElementById("log").innerHTML = "";
}

function runAI() {
  clearLog();

  const input = document.getElementById("userInput").value.toLowerCase();

  // STEP 1: Parsing
  logStep("Parsing input...", "step");

  setTimeout(() => {
    
    // STEP 2: Logic
    logStep("Applying logic engine...", "step");

    setTimeout(() => {

      // STEP 3: Rules
      logStep("Evaluating rules...", "step");

      let risk = "low";

      if (input.includes("fraud") || input.includes("hack")) {
        risk = "high";
      }

      setTimeout(() => {

        // STEP 4: Authority Gate
        logStep("Authority Gate check (QGED)...", "step");

        setTimeout(() => {

          if (risk === "high") {
            logStep("❌ BLOCKED: Policy violation detected", "blocked");
          } else {
            logStep("✔ APPROVED: Execution allowed", "approved");
          }

        }, 800);

      }, 800);

    }, 800);

  }, 800);
}