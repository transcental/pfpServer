# PFP Server

This is a super basic Flask server for serving my pfps. There are three routes:

- `/` - Returns a random pfp
- `/<folder>` - Returns a random pfp from the specified folder
- `/<folder>/<pfp>` - Returns the specified pfp from the specified folder

## Usage

- Clone the repo
- Install the requirements with `pip install -r requirements.txt`
- Run the server with `gunicorn -w 4 -b 0.0.0.0:8000 main:app`
- Access the server at `http://localhost:8000/`
