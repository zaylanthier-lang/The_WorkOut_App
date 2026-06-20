import { useState } from "react";

function Register({ setUser }) {
  const [form, setForm] = useState({
    username: "",
    age: "",
    gender: "",
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleRegister() {
    fetch("http://127.0.0.1:5555/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify(form),
    })
      .then((r) => r.json())
      .then((data) => setUser(data));
  }

  return (
    <div className="page">
      <h1>Register</h1>

      <input name="username" placeholder="Username" onChange={handleChange} />
      <input name="age" placeholder="Age" onChange={handleChange} />
      <input name="gender" placeholder="Gender" onChange={handleChange} />

      <button onClick={handleRegister}>Create Account</button>
    </div>
  );
}

export default Register;