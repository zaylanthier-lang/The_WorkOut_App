from config import db


# -------------------
# USER MODEL
# -------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    workout_logs = db.relationship(
        "WorkoutLog",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"


# -------------------
# EXERCISE MODEL
# -------------------
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


# -------------------
# WORKOUT LOG MODEL
# -------------------
class WorkoutLog(db.Model):
    __tablename__ = "workout_logs"

    id = db.Column(db.Integer, primary_key=True)

    # NEW FIELD (IMPORTANT)
    exercise_name = db.Column(db.String, nullable=False)

    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)

    # AUTH LINK
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

    # RELATIONSHIPS
    user = db.relationship("User", back_populates="workout_logs")
    exercise = db.relationship("Exercise", back_populates="workout_logs")

    def __repr__(self):
        return f"<WorkoutLog {self.id}>"