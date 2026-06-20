from flask import Flask, request, jsonify, session
from flask_cors import CORS

from config import db, migrate
from models import User, Exercise, WorkoutLog

app = Flask(__name__)

# -------------------
# CONFIG
# -------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "super-secret-key"

# -------------------
# CORS (FIXED)
# -------------------
CORS(
    app,
    supports_credentials=True,
    origins=["http://127.0.0.1:5173", "http://localhost:5173"]
)

# -------------------
# INIT
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
# AUTH
# -------------------
@app.post("/api/register")
def register():
    data = request.get_json()

    user = User(
        username=data["username"],
        age=data["age"],
        gender=data["gender"]
    )

    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id

    return user.to_dict(), 201


@app.post("/api/login")
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user:
        return {"error": "User not found"}, 404

    session["user_id"] = user.id

    return user.to_dict(), 200


@app.delete("/api/logout")
def logout():
    session.pop("user_id", None)
    return {"message": "Logged out"}, 200

# -------------------
# EXERCISES
# -------------------
@app.get("/api/exercises")
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([ex.to_dict() for ex in exercises])

# -------------------
# WORKOUT LOGS (FIXED)
# -------------------
@app.get("/api/workout_logs")
def get_workout_logs():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    logs = WorkoutLog.query.filter_by(user_id=user_id).all()

    return jsonify([log.to_dict() for log in logs])


@app.post("/api/workout_logs")
def create_workout_log():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    try:
        log = WorkoutLog(
            exercise_name=data["exercise_name"],
            weight=float(data["weight"]),
            reps=int(data["reps"]),
            sets=int(data["sets"]),
            date=data["date"],
            user_id=user_id
        )

        db.session.add(log)
        db.session.commit()

        return log.to_dict(), 201

    except Exception as e:
        return {"error": str(e)}, 500


@app.delete("/api/workout_logs/<int:id>")
def delete_workout(id):
    user_id = session.get("user_id")

    log = WorkoutLog.query.get(id)

    if not log:
        return {"error": "Not found"}, 404

    if log.user_id != user_id:
        return {"error": "Forbidden"}, 403

    db.session.delete(log)
    db.session.commit()

    return {"message": "Deleted"}, 200


@app.patch("/api/workout_logs/<int:id>")
def update_workout(id):
    user_id = session.get("user_id")

    log = WorkoutLog.query.get(id)

    if not log:
        return {"error": "Not found"}, 404

    if log.user_id != user_id:
        return {"error": "Forbidden"}, 403

    data = request.get_json()

    log.exercise_name = data.get("exercise_name", log.exercise_name)
    log.weight = data.get("weight", log.weight)
    log.reps = data.get("reps", log.reps)
    log.sets = data.get("sets", log.sets)
    log.date = data.get("date", log.date)

    db.session.commit()

    return log.to_dict(), 200

# -------------------
# ERROR HANDLER
# -------------------
@app.errorhandler(Exception)
def handle_error(e):
    return {"error": str(e)}, 500

# -------------------
# RUN
# -------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5555)
