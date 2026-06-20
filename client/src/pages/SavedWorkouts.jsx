import { useEffect, useState } from "react";

function SavedWorkouts() {
  const [logs, setLogs] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/workout_logs", {
      credentials: "include", // IMPORTANT for session login
    })
      .then(async (res) => {
        const data = await res.json();

        if (!res.ok) {
          throw new Error(data.error || "Failed to load logs");
        }

        return data;
      })
      .then((data) => setLogs(Array.isArray(data) ? data : []))
      .catch((err) => setError(err.message));
  }, []);

  if (error) {
    return <div className="page">Error: {error}</div>;
  }

  return (
    <div className="page">
      <h1>Saved Workouts</h1>

      <div className="grid">
        {logs.map((log) => (
          <div className="card" key={log.id}>
            <h3>{log.exercise_name}</h3>
            <p>{log.weight} lbs</p>
            <p>{log.sets} sets</p>
            <p>{log.reps} reps</p>
            <p>{log.date}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SavedWorkouts;