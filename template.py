import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

# list of names to create file and directory
list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'app.py',
    'store_index.py',
    'static',
    'research',
    'templates/chat.html'
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating file: {filepath}")

    else:
        logging.info(f"file {filename} already exists: {filepath}")