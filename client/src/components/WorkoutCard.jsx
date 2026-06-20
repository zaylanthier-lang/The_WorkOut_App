function WorkoutCard({ log, onDelete, onEdit }) {
  return (
    <div className="card">
      <h3>{log.weight} lbs</h3>

      <p>
        {log.sets} sets × {log.reps} reps
      </p>

      <p>{log.date}</p>

      <button onClick={() => onEdit(log)}>
        Edit
      </button>

      <button onClick={() => onDelete(log.id)}>
        Delete
      </button>
    </div>
  );
}

export default WorkoutCard;