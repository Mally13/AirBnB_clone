#!/usr/bin/python3

#
import json

students = {
    "id" : "877",
    "name" : "Kyalo"
}

student_json = json.dumps(students)

student_dict = json.loads(student_json)
print(student_dict)
