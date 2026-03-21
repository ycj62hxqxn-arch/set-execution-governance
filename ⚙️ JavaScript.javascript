function runFlow() {
  const steps = [
    "Parsing Input...",
    "Applying Logic (Usul Engine)...",
    "Evaluating Rules (Qawaid)...",
    "Running Multi-Model Simulation...",
    "Authority Gate (QGED)...",
    "Decision Approved ✔"
  ];

  let i = 0;
  const box = document.getElementById("step");

  const interval = setInterval(() => {
    box.innerText = steps[i];
    box.classList.add("active-step");

    i++;
    if (i >= steps.length) {
      clearInterval(interval);
    }
  }, 1200);
}