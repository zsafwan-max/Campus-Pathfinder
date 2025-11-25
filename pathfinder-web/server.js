// server.js
// Backend for Pathfinder Web Project
// Uses Express.js and Python integration

const express = require("express");
const { PythonShell } = require("python-shell");
const app = express();
const port = 5000;

app.use(express.json());

// Endpoint to run the Python pathfinding script
app.post("/find-path", (req, res) => {
  const { start, end, mode } = req.body;

  if (!start || !end) {
    return res.status(400).json({ error: "Please provide start and end points." });
  }

  // Options for running the Python script
  const options = {
    mode: "json",
    pythonOptions: ["-u"],
    scriptPath: "../Pathfinder project", // <-- update this to your actual folder path
    args: [start, end, mode || "normal"]
  };

  PythonShell.run("pathFindUpdate.py", options)
    .then(results => {
      res.json(results[0]); // Send back Python script output
    })
    .catch(err => {
      console.error("Error running Python script:", err);
      res.status(500).json({ error: "Failed to compute path." });
    });
});

// Start the server
app.listen(port, () => {
  console.log(`Pathfinder backend running on http://localhost:${port}`);
});