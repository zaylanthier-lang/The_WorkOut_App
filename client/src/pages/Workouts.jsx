import { useEffect, useState } from "react";

function Workouts() {
  const [logs, setLogs] = useState([]);

  const [form, setForm] = useState({
    weight: "",
    sets: "",
    reps: "",
    date: "",
  });

  // GET all workouts
  useEffect(() => {
    fetch("http://127.0.0.1:5555/workout_logs")
      .then((r) => r.json())
      .then((data) => setLogs(data));
  }, []);

  // handle input changes
  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  // POST workout (THIS IS THE FIRST ONE YOU WERE ASKING ABOUT)
  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://127.0.0.1:5555/workout_logs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        weight: form.weight,
        sets: form.sets,
        reps: form.reps,
        date: form.date,

        // REQUIRED by backend
        user_id: 1,
        exercise_id: 1,
      }),
    })
      .then((r) => r.json())
      .then((newLog) => {
        setLogs((prev) => [...prev, newLog]);

        setForm({
          weight: "",
          sets: "",
          reps: "",
          date: "",
        });
      });
  }

  return (
    <div className="page">
      <h1>Workouts</h1>

      {/* FORM */}
      <form onSubmit={handleSubmit}>
        <input
          name="weight"
          placeholder="Weight"
          value={form.weight}
          onChange={handleChange}
        />

        <input
          name="sets"
          placeholder="Sets"
          value={form.sets}
          onChange={handleChange}
        />

        <input
          name="reps"
          placeholder="Reps"
          value={form.reps}
          onChange={handleChange}
        />

        <input
          type="date"
          name="date"
          value={form.date}
          onChange={handleChange}
        />

        <button type="submit">Add Workout</button>
      </form>

      {/* DISPLAY */}
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

export default Workouts;