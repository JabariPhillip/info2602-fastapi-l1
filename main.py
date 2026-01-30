from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'


@app.get('/shuttles')
async def get_shuttles_overview():
    shuttles_list = []

    for shuttle in data:
        curr_data = {
            "name": shuttle['name'],
            "reg_no": shuttle['vehicle_details']['reg_no'],
            "active": shuttle['active'],
        }
        shuttles_list.append(curr_data)
    return shuttles_list