// server.js
// Backend for Pathfinder Web Project
// Uses Express.js and PythonShell to run Python pathfinder

const express = require("express");
const { PythonShell } = require("python-shell");
const path = require("path");
const app = express();
const port = 5000;

app.use(express.json());

// Endpoint to run Python pathfinding
app.post("/find-path", (req, res) => {
  const { start, end, mode } = req.body;

  if (!start || !end) {
    return res.status(400).json({ error: "Please provide start and end points." });
  }

  // Correct script path — points to your Python folder
  const scriptPath = path.join(__dirname, "../../Pathfinder_project");

  const options = {
    mode: "json",
    pythonOptions: ["-u"],
    scriptPath: scriptPath,
    args: [start, end, mode || "shortest"]
  };

  PythonShell.run("pathFindupdate.py", options)
    .then(results => {
      res.json(results[0]); // return Python JSON output
    })
    .catch(err => {
      console.error("Error running Python script:", err);
      res.status(500).json({ error: "Failed to compute path." });
    });
});

app.listen(port, () => {
  console.log(`Pathfinder backend running at http://localhost:${port}`);
});