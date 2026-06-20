from flask import Flask, request, jsonify
from flask_cors import CORS

from config import db, migrate
from models import User, Exercise, WorkoutLog

app = Flask(__name__)

# -------------------
# CONFIG
# -------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# -------------------
# CORS
# -------------------
CORS(app, resources={r"/*": {"origins": "*"}})

# -------------------
# INIT DB + MIGRATE
# -------------------
db.init_app(app)
migrate.init_app(app, db)

# -------------------
# HOME
# -------------------
@app.get("/")
def home():
    return {"message": "Workout Tracker API"}

# -------------------
# EXERCISES
# -------------------
@app.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": ex.id,
            "name": ex.name,
            "muscle_group": ex.muscle_group
        }
        for ex in exercises
    ])


@app.post("/exercises")
def create_exercise():
    data = request.get_json()

    exercise = Exercise(
        name=data["name"],
        muscle_group=data["muscle_group"]
    )

    db.session.add(exercise)
    db.session.commit()

    return {
        "id": exercise.id,
        "name": exercise.name,
        "muscle_group": exercise.muscle_group
    }, 201

# -------------------
# USERS
# -------------------
@app.get("/users")
def get_users():
    users = User.query.all()

    return jsonify([
        {
            "id": user.id,
            "username": user.username,
            "age": user.age,
            "gender": user.gender
        }
        for user in users
    ])


@app.post("/users")
def create_user():
    data = request.get_json()

    user = User(
        username=data["username"],
        age=data["age"],
        gender=data["gender"]
    )

    db.session.add(user)
    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
        "age": user.age,
        "gender": user.gender
    }, 201

# -------------------
# WORKOUT LOGS (FULL CRUD)
# -------------------
@app.get("/workout_logs")
def get_workout_logs():
    logs = WorkoutLog.query.all()

    return jsonify([
        {
            "id": log.id,
            "exercise_name": log.exercise_name,
            "weight": log.weight,
            "reps": log.reps,
            "sets": log.sets,
            "date": log.date,
            "user_id": log.user_id,
            "exercise_id": log.exercise_id
        }
        for log in logs
    ])


@app.post("/workout_logs")
def create_workout_log():
    data = request.get_json()

    log = WorkoutLog(
        exercise_name=data["exercise_name"],
        weight=float(data["weight"]),
        reps=int(data["reps"]),
        sets=int(data["sets"]),
        date=data["date"],
        user_id=data["user_id"],
        exercise_id=data["exercise_id"]
    )

    db.session.add(log)
    db.session.commit()

    return {
        "id": log.id,
        "exercise_name": log.exercise_name,
        "weight": log.weight,
        "reps": log.reps,
        "sets": log.sets,
        "date": log.date,
        "user_id": log.user_id,
        "exercise_id": log.exercise_id
    }, 201


@app.delete("/workout_logs/<int:id>")
def delete_workout(id):
    log = WorkoutLog.query.get(id)

    if not log:
        return {"error": "Workout not found"}, 404

    db.session.delete(log)
    db.session.commit()

    return {"message": "Workout deleted"}, 200


@app.patch("/workout_logs/<int:id>")
def update_workout(id):
    log = WorkoutLog.query.get(id)

    if not log:
        return {"error": "Workout not found"}, 404

    data = request.get_json()

    log.exercise_name = data.get("exercise_name", log.exercise_name)
    log.weight = data.get("weight", log.weight)
    log.reps = data.get("reps", log.reps)
    log.sets = data.get("sets", log.sets)
    log.date = data.get("date", log.date)

    db.session.commit()

    return {
        "id": log.id,
        "exercise_name": log.exercise_name,
        "weight": log.weight,
        "reps": log.reps,
        "sets": log.sets,
        "date": log.date,
        "user_id": log.user_id,
        "exercise_id": log.exercise_id
    }, 200

# -------------------
# RUN APP
# -------------------
if __name__ == "__main__":
    app.run(port=5555, debug=True)