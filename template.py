import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

files_list = [
    "src/__init__.py",
    "src/__helper__.py",
    "src/__prompt__.py",
    ".env",
    "setup.py",
    "app.py",
    "store_index.py",
    "static",
    "templates/chat.html"
]

for filepath in files_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")
