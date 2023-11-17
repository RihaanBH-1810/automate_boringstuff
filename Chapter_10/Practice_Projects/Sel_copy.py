import shutil
from pathlib import Path
import os


ex = ".py"
folder = Path.cwd()
print(f"Searching in {folder}for files with extensions of type {ex}")
for folder, subfs, files in os.walk(folder):
    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension == ex:
            fileAbsPath = folder + os.path.sep + filename
            print('Copying file from ', fileAbsPath, 'to', "/home/rihaan_180/Desktop/Copies")
            shutil.copy(fileAbsPath, f"/home/rihaan_180/Desktop/Copies")




