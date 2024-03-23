# Task Catalog App Backend
## via FastAPI

## Table of Contents
- [Installation](#installation)
- [Features](#features)
  - [Backend](#backend)
  - [Database](#database)
  - [Docker-compose](#Docker-compose)
- [Testing](#testing)

---

## Installation

To run the Task Catalog App, use Docker with docker-compose:

Run the following command in your terminal: ``docker-compose -d --build``

Access the app at: [http://127.0.0.1:7000/](http://127.0.0.1:7000/)

Access the backend API at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Features

- Database powered by Redis for high performance.
- FastAPI for the backend, implementing CRUD operations (refer to the backend readme for more details).
- Docker-compose to seamlessly integrate all services.
- Backend unit tests for robust functionality.

### Backend

Utilizing FastAPI for efficient backend development.

### Frontend

Employing Streamlit for a clean and intuitive frontend experience.

### Database

The app utilizes Redis, serving as an in-memory data structure store, distributed key–value database, cache, and message broker with optional durability.

### Docker-compose

1. Backend (FastAPI)
2. Frontend (Streamlit)
3. Database (Redis)

---


## Testing

1. Comment in backend/main.py lines 6 & 7 and uncomment lines 10 & 11.
2. Run this command: `docker-compose run --service-ports backend bash`
3. Run: `pytest`
#### Results:
`python app/backend/test_main.py`