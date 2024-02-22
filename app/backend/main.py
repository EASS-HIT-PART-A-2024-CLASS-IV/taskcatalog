from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional, List

import redis
from models import Task
from database import local_db, redis_con, convertor

# Just for testing
# from .models import Catalog
# from .database import local_db, redis_con, convertor

import json

import uvicorn

app = FastAPI(title="To-do List API")

#This will make a Task Catalog
class Catalog(BaseModel):
    tasks: List[Task]


store_catalog = []


# Create, Read, Update, Delete

@app.get('/')
async def home():
    return {"Hello": "World"}

@app.post('/catalog/')
async def create_catalog(task: Task):
    task_dict = task.dict()
    redis_con.hmset(task_dict.get('title'), task.dict())

    return store_catalog

@app.get('/catalog/', response_model=List[Task])
async def get_all_tasks():
    store_catalog_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_catalog_redis.append(row)

    return store_catalog_redis

@app.get('/catalog/{title}')
async def get_task(title: str):
    store_catalog_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_catalog_redis.append(row)
    
    return {}

        

@app.put('/catalog/{title}')
async def update_task(title: str, task: Task):

    if redis_con.hgetall(title):
        # update value in here
        if title == task.title:
            redis_con.hset(title, 'description', task.description)
            redis_con.hset(title, 'due_date', task.due_date)

    return task.dict()
    


@app.delete('/catalog/{title}')
async def delete_task(title: str):

    # get a value given a key
    if redis_con.hgetall(title):
        # Delete a row given hash key
        redis_con.delete(title)
    
    store_catalog_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_catalog_redis.append(row)
    
    return {}
    

if __name__ == "__main__":
    uvicorn.run(app)
