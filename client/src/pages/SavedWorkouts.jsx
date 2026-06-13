import { useEffect, useState } from "react";

function SavedWorkouts() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/workout_logs")
      .then((r) => r.json())
      .then(setLogs);
  }, []);

  return (
    <div className="page">
      <h1>Saved Workouts</h1>

      <div className="grid">
        {logs.map((log) => (
          <div className="card" key={log.id}>
            <h3>{log.weight} lbs</h3>
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