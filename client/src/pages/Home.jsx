import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home-container">
      {/* BIG TITLE */}
      <h1 className="main-title">LiftTracker</h1>

      <p className="subtitle">
        Track your workouts, build strength, and stay consistent.
      </p>

      {/* NAV BUTTONS */}
      <div className="home-buttons">
        <Link to="/exercises" className="home-btn">
          Exercises
        </Link>

        <Link to="/workouts" className="home-btn">
          Workouts
        </Link>
      </div>
    </div>
  );
}

export default Home;