import { Link } from "react-router-dom";

function Navbar({ user, setUser }) {
  function handleLogout() {
    fetch("http://127.0.0.1:5555/api/logout", {
      method: "DELETE",
      credentials: "include",
    }).then(() => setUser(null));
  }

  return (
    <nav className="navbar">
      <Link to="/" className="logo">
        🏋️ LiftTracker
      </Link>

      <div className="nav-links">
        <Link to="/workouts">Workouts</Link>
        <Link to="/exercises">Exercises</Link>
        <Link to="/history">History</Link>

        {!user ? (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        ) : (
          <button onClick={handleLogout}>Logout</button>
        )}
      </div>
    </nav>
  );
}

export default Navbar;