function ExerciseCard({ exercise }) {
  return (
    <div className="card">
      <h3>{exercise.name}</h3>
      <p>{exercise.muscle_group}</p>
    </div>
  );
}

export default ExerciseCard;