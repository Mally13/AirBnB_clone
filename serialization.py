#!/usr/bin/python3

#importing the module
import json

students = {
    "id" : "877",
    "name" : "Kyalo"
}

#serializing JSON
student_json = json.dumps(students)

print(student_json)
