// server.js
// Backend for Pathfinder Web Project
// Use Express.js and PythonShell to run Python pathfinder

const express = require("express");
const { PythonShell } = require("python-shell");
const path = require("path");
const app = express();
const port = 5001; 

app.use(express.json());

// Add a root route for testing
app.get("/", (req, res) => {
  res.send("Pathfinder backend is running!");
});

app.post("/find-path", (req, res) => {
  const { start, end, mode } = req.body;

  console.log("Received request:", start, end, mode);

  if (!start || !end) {
    return res.status(400).json({ error: "Please provide start and end points." });
  }

  
  const scriptPath = path.join(__dirname, "../Pathfinder_project");
  console.log("Using scriptPath:", scriptPath);

  const options = {
    mode: "json",
    pythonOptions: ["-u"],
    scriptPath: scriptPath,
    pythonPath: "/Library/Frameworks/Python.framework/Versions/3.11/bin/python3",
    args: [start, end, mode || "shortest"]
  };

  console.log("PythonShell options:", options);

  PythonShell.run("pathFindupdate.py", options)
    .then(results => {
      console.log("Python returned:", results);
      res.json(results[0] || {});
    })
    .catch(err => {
      console.error("Error running Python script:", err);
      res.status(500).json({ error: "Failed to compute path." });
    });
});

// Adding error handling for server startup
const server = app.listen(port, () => {
  console.log(`Pathfinder backend running at http://localhost:${port}`);
}).on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${port} is already in use. Please use a different port.`);
  } else {
    console.error('Server failed to start:', err);
  }
  process.exit(1);
});

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.log('\nShutting down server...');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});

// Keep the process alive - handle uncaught errors
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

console.log("Starting server...");