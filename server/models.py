from config import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    workout_logs = db.relationship(
        "WorkoutLog",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    muscle_group = db.Column(db.String, nullable=False)

    workout_logs = db.relationship(
        "WorkoutLog",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Exercise {self.name}>"


class WorkoutLog(db.Model):
    __tablename__ = "workout_logs"

    id = db.Column(db.Integer, primary_key=True)

    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)

    date = db.Column(db.String, nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="workout_logs"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_logs"
    )

    def __repr__(self):
        return f"<WorkoutLog {self.id}>"