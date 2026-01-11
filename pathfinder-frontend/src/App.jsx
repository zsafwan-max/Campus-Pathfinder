import { useState } from "react";
import "./App.css";

const BUILDINGS = [
  "Parking Garage",
  "Core Science Facility",
  "University Centre",
  "Earth Science Building",
  "Engineering Building",
  "Business Building",
  "Chapel",
  "Dorms",
  "Chemistry/Physics Building",
  "Old Science Building",
  "Arts & Administration",
  "Bruneau Centre",
  "Library",
  "HKR (Human Kinetics)",
  "The Works (Recreation)",
  "Education Building",
];

function App() {
  const [start, setStart] = useState("Library");
  const [end, setEnd] = useState("Engineering Building");
  const [mode, setMode] = useState("shortest");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  function handleFindPath() {
    setError("");
    setResult(null);

    // For now, just show what user selected (API next step)
    setResult({
      path: [{ from: start, to: end, label: mode }],
      total_time: 0,
    });
  }

  return (
    <div style={{ padding: "20px", maxWidth: "700px" }}>
      <h1>Campus Pathfinder</h1>
      <p>Find the best route between campus buildings.</p>

      <div style={{ display: "grid", gap: "12px", marginTop: "20px" }}>
        <label>
          Start building:
          <select
            value={start}
            onChange={(e) => setStart(e.target.value)}
            style={{ display: "block", width: "100%", padding: "10px", marginTop: "6px" }}
          >
            {BUILDINGS.map((b) => (
              <option key={b} value={b}>
                {b}
              </option>
            ))}
          </select>
        </label>

        <label>
          Destination building:
          <select
            value={end}
            onChange={(e) => setEnd(e.target.value)}
            style={{ display: "block", width: "100%", padding: "10px", marginTop: "6px" }}
          >
            {BUILDINGS.map((b) => (
              <option key={b} value={b}>
                {b}
              </option>
            ))}
          </select>
        </label>

        <label>
          Mode:
          <select
            value={mode}
            onChange={(e) => setMode(e.target.value)}
            style={{ display: "block", width: "100%", padding: "10px", marginTop: "6px" }}
          >
            <option value="shortest">Shortest</option>
            <option value="accessible">Accessible</option>
          </select>
        </label>

        <button
          onClick={handleFindPath}
          style={{
            padding: "12px",
            fontSize: "16px",
            cursor: "pointer",
            marginTop: "10px",
          }}
        >
          Find Path
        </button>
      </div>

      {error && (
        <div style={{ marginTop: "20px", color: "crimson" }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div style={{ marginTop: "25px", padding: "15px", border: "1px solid #ccc" }}>
          <h2>Route Result</h2>
          <p>
            <strong>Total Time:</strong> {result.total_time} minutes
          </p>

          <ol>
            {result.path.map((step, idx) => (
              <li key={idx}>
                {step.from} → {step.to} ({step.label})
              </li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}

export default App;