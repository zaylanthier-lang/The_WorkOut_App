import { useEffect, useState } from "react";
import WorkoutCard from "../components/WorkoutCard";

function Workouts() {
  const [logs, setLogs] = useState([]);

  const [form, setForm] = useState({
    weight: "",
    sets: "",
    reps: "",
    date: "",
  });

  const [editingId, setEditingId] = useState(null);

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

  // DELETE workout
  function handleDelete(id) {
    fetch(`http://127.0.0.1:5555/workout_logs/${id}`, {
      method: "DELETE",
    }).then(() => {
      setLogs((prev) => prev.filter((log) => log.id !== id));
    });
  }

  // EDIT workout (fills form)
  function handleEdit(log) {
    setForm({
      weight: log.weight,
      sets: log.sets,
      reps: log.reps,
      date: log.date,
    });

    setEditingId(log.id);
  }

  // CREATE or UPDATE workout
  function handleSubmit(e) {
    e.preventDefault();

    const url = editingId
      ? `http://127.0.0.1:5555/workout_logs/${editingId}`
      : "http://127.0.0.1:5555/workout_logs";

    const method = editingId ? "PATCH" : "POST";

    fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        weight: form.weight,
        sets: form.sets,
        reps: form.reps,
        date: form.date,
        user_id: 1,
        exercise_id: 1,
      }),
    })
      .then((r) => r.json())
      .then((data) => {
        if (editingId) {
          setLogs((prev) =>
            prev.map((log) =>
              log.id === editingId ? data : log
            )
          );
        } else {
          setLogs((prev) => [...prev, data]);
        }

        setForm({
          weight: "",
          sets: "",
          reps: "",
          date: "",
        });

        setEditingId(null);
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

        <button type="submit">
          {editingId ? "Update Workout" : "Add Workout"}
        </button>
      </form>

      {/* CARDS */}
      <div className="grid">
        {logs.map((log) => (
          <WorkoutCard
            key={log.id}
            log={log}
            onDelete={handleDelete}
            onEdit={handleEdit}
          />
        ))}
      </div>
    </div>
  );
}

export default Workouts;