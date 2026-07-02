# User Table

Keeps a local database of simple user data.
Local database saves/reads in the same directory as users.db.

## Installation

- `py -m venv .venv` to create a python environment.
- `source .venv/Scripts/activate` to start the environment.
- `py -m pip install -r requirements.txt` to install python requirements to the environment.
- `flask run` to start server and create the database.

## Routes

- `/` : Gets health of server.
- `/routes` : Gets a list of routes, methods, and data.
- `GET /api/users` : Gets a list of the users currently in the database.
- `POST /api/users/add` : Add a user to the database.
  - Required header: "Content-Type" : "application/json"
  - Body format:
  ```json
    {
    "name": string,
    "email": string
    }
  ```
