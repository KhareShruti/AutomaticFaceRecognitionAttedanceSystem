import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-4e021-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students') 

data = {
    "321654":
        {
            "Name": "Shruti Khare",
            "Major": "Data Analytics",
            "Starting_year": 2021,
            "Total_attendance": 7,
            "Grade": "A+",
            "Year": 3,
            "Last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "Name": "Emly Blunt",
            "Major": "Economics",
            "Starting_year": 2022,
            "Total_attendance": 12,
            "Grade": "B",
            "Year": 1,
            "Last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "Name": "Elon Musk",
            "Major": "Physics",
            "Starting_year": 2020,
            "Total_attendance": 7,
            "Grade": "A",
            "Year": 2,
            "Last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
