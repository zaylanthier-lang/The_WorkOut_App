import { useState } from "react";

function Login({ setUser }) {
  const [username, setUsername] = useState("");

  function handleLogin() {
    fetch("http://127.0.0.1:5555/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ username }),
    })
      .then((r) => r.json())
      .then((data) => setUser(data));
  }

  return (
    <div className="page">
      <h1>Login</h1>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;