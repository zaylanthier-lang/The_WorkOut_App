import { useEffect, useState } from "react";
import ExerciseCard from "../components/ExcerciseCard";

function Exercises() {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/exercises", {
  credentials: "include",
})
      .then((r) => r.json())
      .then(setExercises);
  }, []);

  return (
    <div>
      <h1>Exercises</h1>

      {exercises.map((exercise) => (
        <ExerciseCard key={exercise.id} exercise={exercise} />
      ))}
    </div>
  );
}

export default Exercises;