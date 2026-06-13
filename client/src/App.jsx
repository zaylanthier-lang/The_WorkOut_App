import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Exercises from "./pages/Exercises";
import Workouts from "./pages/Workouts";
import SavedWorkouts from "./pages/SavedWorkouts";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/exercises" element={<Exercises />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/history" element={<SavedWorkouts />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;