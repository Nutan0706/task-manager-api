# Task Manager API

This is a simple Task Manager API built with FastAPI and PostgreSQL.

## Requirements
- Docker
- Docker Compose

## How to Run

1. Clone the repository.
2. Run:

## Use below command to Run this project

1. docker-compose up --build
     - It builds the FastAPI app image.
     - Pulls the official Postgres image.
     - Starts both containers.
     - Connects FastAPI app with Postgres automatically.
2. How to Access the application
     - http://localhost:8000/docs

## API Tests

1. Create Task (POST /tasks)
    - curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"title":"My Task","description":"Testing Task Creation"}'
2. Get all Tasks (GET /tasks)
    - curl http://localhost:8000/tasks
3. Get Task by ID (GET /tasks/1)
    - curl http://localhost:8000/tasks/1
4. Update Task (PUT /tasks/1)
    - curl -X PUT "http://localhost:8000/tasks/1" -H "Content-Type: application/json" -d '{"title":"Updated Task","description":"Updated Description","completed":true}'
5. Delete Task (DELETE /tasks/1)
    - curl -X DELETE http://localhost:8000/tasks/1
