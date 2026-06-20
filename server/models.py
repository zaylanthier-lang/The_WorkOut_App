from config import db
from datetime import date

# -------------------
# USER MODEL
# -------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    workout_logs = db.relationship(
        "WorkoutLog",
        backref="user",
        cascade="all, delete",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "age": self.age,
            "gender": self.gender
        }


# -------------------
# EXERCISE MODEL
# -------------------
class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "muscle_group": self.muscle_group
        }


# -------------------
# WORKOUT LOG MODEL
# -------------------
class WorkoutLog(db.Model):
    __tablename__ = "workout_logs"

    id = db.Column(db.Integer, primary_key=True)

    exercise_name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "exercise_name": self.exercise_name,
            "weight": self.weight,
            "reps": self.reps,
            "sets": self.sets,
            "date": self.date,
            "user_id": self.user_id
        }