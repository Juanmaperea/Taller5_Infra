Students System - Separated frontend, backend, and Postgres using Docker Compose

How to run (requires Docker and Docker Compose):
1. From project root run:
   docker compose up --build

2. Open:
   - Frontend: http://localhost:8080
   - Backend docs: http://localhost:8000/docs

Notes:
- The frontend uses fetch to call http://localhost:8000/students when run locally.
- Inside Docker Compose the backend can reach Postgres at host 'db'.
- To persist data, the postgres_data volume is mounted.
