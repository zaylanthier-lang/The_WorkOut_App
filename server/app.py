from flask import Flask, request, jsonify
from flask_cors import CORS

from config import db, migrate
from models import User, Exercise, WorkoutLog

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

CORS(app)


@app.route("/")
def home():
    return {"message": "Workout Tracker API"}


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
# EXERCISES
# -------------------

@app.get("/exercises")
def get_exercises():

    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": exercise.id,
            "name": exercise.name,
            "muscle_group": exercise.muscle_group
        }
        for exercise in exercises
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


@app.patch("/exercises/<int:id>")
def update_exercise(id):

    exercise = Exercise.query.get_or_404(id)

    data = request.get_json()

    exercise.name = data.get("name", exercise.name)
    exercise.muscle_group = data.get(
        "muscle_group",
        exercise.muscle_group
    )

    db.session.commit()

    return {
        "message": "Exercise updated"
    }


@app.delete("/exercises/<int:id>")
def delete_exercise(id):

    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return {
        "message": "Exercise deleted"
    }


# -------------------
# WORKOUT LOGS
# -------------------

@app.get("/workout_logs")
def get_workout_logs():

    logs = WorkoutLog.query.all()

    return jsonify([
        {
            "id": log.id,
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
        weight=data["weight"],
        reps=data["reps"],
        sets=data["sets"],
        date=data["date"],
        user_id=data["user_id"],
        exercise_id=data["exercise_id"]
    )

    db.session.add(log)
    db.session.commit()

    return {
        "message": "Workout log created",
        "id": log.id
    }, 201


@app.patch("/workout_logs/<int:id>")
def update_workout_log(id):

    log = WorkoutLog.query.get_or_404(id)

    data = request.get_json()

    log.weight = data.get("weight", log.weight)
    log.reps = data.get("reps", log.reps)
    log.sets = data.get("sets", log.sets)
    log.date = data.get("date", log.date)

    db.session.commit()

    return {
        "message": "Workout updated"
    }


@app.delete("/workout_logs/<int:id>")
def delete_workout_log(id):

    log = WorkoutLog.query.get_or_404(id)

    db.session.delete(log)
    db.session.commit()

    return {
        "message": "Workout deleted"
    }


if __name__ == "__main__":
    app.run(port=5555, debug=True)