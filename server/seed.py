from app import app
from config import db
from models import User, Exercise, WorkoutLog


with app.app_context():

    # Clear existing data
    WorkoutLog.query.delete()
    Exercise.query.delete()
    User.query.delete()

    # Create users
    user1 = User(
        username="Zayden",
        age=20,
        gender="Male"
    )

    user2 = User(
        username="Sarah",
        age=25,
        gender="Female"
    )

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create exercises
    bench = Exercise(
        name="Bench Press",
        muscle_group="Chest"
    )

    squat = Exercise(
        name="Squat",
        muscle_group="Legs"
    )

    deadlift = Exercise(
        name="Deadlift",
        muscle_group="Back"
    )

    shoulder_press = Exercise(
        name="Shoulder Press",
        muscle_group="Shoulders"
    )

    barbell_row = Exercise(
        name="Barbell Row",
        muscle_group="Back"
    )

    db.session.add_all([
        bench,
        squat,
        deadlift,
        shoulder_press,
        barbell_row
    ])

    db.session.commit()

    # Create workout logs
    workout1 = WorkoutLog(
        weight=185,
        reps=5,
        sets=3,
        date="2026-06-10",
        user_id=user1.id,
        exercise_id=bench.id
    )

    workout2 = WorkoutLog(
        weight=225,
        reps=5,
        sets=3,
        date="2026-06-10",
        user_id=user1.id,
        exercise_id=squat.id
    )

    workout3 = WorkoutLog(
        weight=95,
        reps=8,
        sets=3,
        date="2026-06-10",
        user_id=user2.id,
        exercise_id=shoulder_press.id
    )

    db.session.add_all([
        workout1,
        workout2,
        workout3
    ])

    db.session.commit()

    print("Database seeded!")