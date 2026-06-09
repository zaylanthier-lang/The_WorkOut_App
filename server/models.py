from config import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

    workout_logs = db.relationship(
        "WorkoutLog",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    muscle_group = db.Column(db.String)

    workout_logs = db.relationship(
        "WorkoutLog",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )


class WorkoutLog(db.Model):
    __tablename__ = "workout_logs"

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    date = db.Column(db.String)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id")
    )

    user = db.relationship(
        "User",
        back_populates="workout_logs"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_logs"
    )