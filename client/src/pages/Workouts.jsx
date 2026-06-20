import { useEffect, useState } from "react";
import WorkoutCard from "../components/WorkoutCard";

function Workouts() {
  const [logs, setLogs] = useState([]);

  const [form, setForm] = useState({
    exercise_name: "",
    weight: "",
    sets: "",
    reps: "",
    date: "",
  });

  // GET workouts
  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/workout_logs", {
      credentials: "include",
    })
      .then((r) => r.json())
      .then(setLogs);
  }, []);

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  // CREATE workout
  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://127.0.0.1:5555/api/workout_logs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({
        exercise_name: form.exercise_name,
        weight: Number(form.weight),
        sets: Number(form.sets),
        reps: Number(form.reps),
        date: form.date,
      }),
    })
      .then((r) => r.json())
      .then((newLog) => {
        setLogs((prev) => [...prev, newLog]);

        setForm({
          exercise_name: "",
          weight: "",
          sets: "",
          reps: "",
          date: "",
        });
      });
  }

  // DELETE workout
  function handleDelete(id) {
    fetch(`http://127.0.0.1:5555/api/workout_logs/${id}`, {
      method: "DELETE",
      credentials: "include",
    }).then(() => {
      setLogs((prev) => prev.filter((log) => log.id !== id));
    });
  }

  return (
    <div className="page">
      <h1>Workouts</h1>

      {/* FORM */}
      <form onSubmit={handleSubmit}>
        <input
          name="exercise_name"
          placeholder="Exercise Name"
          value={form.exercise_name}
          onChange={handleChange}
        />

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
          <WorkoutCard
            key={log.id}
            log={log}
            onDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  );
}

export default Workouts;