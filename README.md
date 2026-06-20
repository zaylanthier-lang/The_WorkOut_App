🏋️ LiftTracker — Full-Stack Workout Tracker
📌 Project Overview

LiftTracker is a full-stack web application that allows users to track their workouts, including exercises, sets, reps, weight, and date. Users can create, view, update, and delete workout logs to help them stay consistent and monitor their progress over time.

This project was built as a capstone to demonstrate full-stack development skills using a React frontend and a Flask backend with a SQLite database.

🚀 Features
Create new workout logs
View all saved workouts
Update existing workouts
Delete workouts
Track exercise name, weight, sets, reps, and date
Responsive and clean UI
Real-time updates between frontend and backend
🧠 Tech Stack
Frontend
React
JavaScript (ES6+)
CSS
Backend
Python
Flask
Flask-CORS
SQLAlchemy
Flask-Migrate
SQLite
📁 Project Structure
project-root/
│
├── client/ (React frontend)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── index.css
│
├── server/ (Flask backend)
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   └── seed.py
│
└── README.md
🔌 API Endpoints
Workout Logs
GET /workout_logs
→ Get all workout logs
POST /workout_logs
→ Create a new workout log
PATCH /workout_logs/<id>
→ Update an existing workout log
DELETE /workout_logs/<id>
→ Delete a workout log
Exercises
GET /exercises
POST /exercises
Users
GET /users
POST /users
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/apwood09/Capstone-Full-Stack-Application.git
2. Backend Setup
cd server
pip install -r requirements.txt
python app.py

Make sure Flask runs on:

http://127.0.0.1:5555
3. Frontend Setup
cd client
npm install
npm run dev

Frontend runs on:

http://127.0.0.1:5173
 How It Works
User adds a workout (exercise name, weight, sets, reps, date)
Data is sent to Flask backend API
Backend stores it in SQLite database
React fetches and displays updated data
User can edit or delete workouts in real time


Home page
Workout page
Edit workout view
🏁 Future Improvements
Add user authentication
Add progress charts (weight over time)
Add exercise dropdown instead of text input
Filter workouts by exercise or date
Deploy full app (Netlify + Render)
👨‍💻 Author

Built by Zayden as a full-stack capstone project to demonstrate CRUD operations, API development, and React frontend integration.