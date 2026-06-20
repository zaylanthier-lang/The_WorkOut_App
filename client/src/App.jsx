import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Workouts from "./pages/Workouts";
import Exercises from "./pages/Exercises";
import SavedWorkouts from "./pages/SavedWorkouts";

function App() {
  const [user, setUser] = useState(null);

  return (
    <BrowserRouter>
      <Navbar user={user} setUser={setUser} />

      <Routes>
        <Route path="/" element={<Home />} />

        {/* AUTH */}
        <Route path="/login" element={<Login setUser={setUser} />} />
        <Route path="/register" element={<Register setUser={setUser} />} />

        {/* PROTECTED ROUTES (simple version) */}
        {user && (
          <>
            <Route path="/workouts" element={<Workouts user={user} />} />
            <Route path="/exercises" element={<Exercises />} />
            <Route path="/history" element={<SavedWorkouts />} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
}

export default App;