# Task Catalog API

* This is a task-catalog API built with FastAPI which is a modern, fast (high-performance), web framework for building APIs.
* data is stored in memory (no database used for now)
* This is currently only Backend at the moment.
* Dockerized so it's simple to install!

## Installation

1. Clone the Project:
```
git clone  https://github.com/EASS-HIT-PART-A-2024-CLASS-IV/taskcatalog.git
```

2. Build the image:
```
docker build -t catalog-api . -f Dockerfile
```
3. Run the image:
```
docker run -ti -p 8888:8086 catalog-api
```
## Features
* Adding a task
* Getting a task
* Getting all tasks
* Remove a task
* Update a task


## Testing
1. Comment in backend/main.py lines 6 & 7 and uncomment lines 10 & 11.
2. run this command: `docker-compose run --service-ports backend bash`
3. last but not least, run: `pytest`

## Screenshot

### The API:
![Api](https://puu.sh/J83Sn/9b74a032e3.png)
### Testing:
![Testing](https://puu.sh/J83Rx/8fcbdfb95f.png)
