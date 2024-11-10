# FarmNote


## Local Setup

### Backend

* Use Pycharm to create new virtual environment or type `python -m venv .venv`
* Install all requirements `python -m pip install -r backend/requirements.txt`
* Start the backend `uvicorn backend.src.app.main:app --host 127.0.0.1 --port 8000 --reload`
* Link to the API docs : `http://127.0.0.1:8000/docs`
* How to run tests From the command line : `pytest .\backend\tests\test_notes_crud.py`

### Frontend

* Install all required npm packages `cd frontend && npm install`
* Start the frontend `npm run dev`


## Environment
`Python 3.12`, `Node.js v20`, 

