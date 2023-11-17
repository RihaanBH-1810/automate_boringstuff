import shutil
from pathlib import Path
import os


dir = Path.cwd()

for folder, subfs, files in os.walk(dir):
    loc_fol = os.path.abspath(folder)
    for filename in files:
        loc = os.path.abspath(filename)
        size = os.path.getsize(loc)
        if size >= 1e8:
            print(f"{filename} located in {loc_fol} has a size of {size} Bytes")
            print("You might have to delete these files to free up space.")
       