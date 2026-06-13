import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      {/* CLICKABLE TITLE */}
      <Link to="/" className="logo">
        🏋️ LiftTracker
      </Link>

      <div className="nav-links">
        <Link to="/exercises">Exercises</Link>
        <Link to="/workouts">Workouts</Link>
        <Link to="/history">History</Link>
      </div>
    </nav>
  );
}

export default Navbar;