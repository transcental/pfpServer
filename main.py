from flask import Flask, send_file
from pathlib import Path
import random

app = Flask(__name__)
pfp_folder = Path("static/pfps")

def get_random_file_from_folder(folder: Path) -> Path:
    files = [file for file in folder.rglob("*") if file.is_file()]

    if files:
        return random.choice(files)
    else:
        return None

@app.route('/')
def random_file():
    pfp = get_random_file_from_folder(pfp_folder)

    if pfp:
        return send_file(pfp)
    else:
        return "No files found", 404


@app.route('/<path:folder>')
def folder(folder: str):
    folder = pfp_folder / folder
    pfp = get_random_file_from_folder(folder)

    if pfp:
        return send_file(pfp)
    else:
        return "No files found", 404


@app.route('/<path:filename>')
def file(filename: str):
    file = pfp_folder / filename
    if file.exists():
        return send_file(file)
    else:
        return "File not found", 404
