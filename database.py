import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendence-realtime-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")  # It will create Students directory in the database
data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "303030":
        {
            "name": "Maaz Karim",
            "major": "NLP",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "E",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "717171":
        {
            "name": "Ankur Singh",
            "major": "Computer Vision",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)  # Will add data to database
