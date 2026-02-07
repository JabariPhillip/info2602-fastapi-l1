from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'
      
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data

#Exercises 1 and 2

@app.get('/stats')
async def get_stats():
    stats = {}

    for student in data:
        pref = student["pref"]
        if pref in stats:
            stats[pref] += 1
        else:
            stats[pref] = 1

        programme = student["programme"]
        if programme in stats:
            stats[programme] += 1
        else:
            stats[programme] = 1

    return stats

@app.get('/add/{a}/{b}')
async def add(a: int, b: int):
    return {"result": a + b}

@app.get('/subtract/{a}/{b}')
async def subtract(a: int, b: int):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def multiply(a: int, b: int):
    return {"result": a * b}

@app.get('/divide/{a}/{b}')
async def divide(a: int, b: int):
    if b > 0:
        return {"result": a / b}
    return{"error": "Can not divide by 0"}