from pathlib import Path
import os, shutil , re

folder = Path.cwd()

files = []

for item in folder.iterdir():
    if item.is_file():
        files.append(item)

search_files = re.compile(r'spam(\d+).txt')

existing_numbers = set()

for file in files:
    match = search_files.match(file.name)
    if match:
        existing_numbers.add(int(match.group(1)))

max_number = max(existing_numbers, default=0)
for expected_number in range(1, max_number + 1):
    if expected_number not in existing_numbers:
        for file in files:
            match = search_files.match(file.name)
            if match and int(match.group(1)) > expected_number:
                new_number = expected_number
                new_name = f'spam{new_number:03d}.txt'
                while new_number in existing_numbers:
                    new_number += 1
                    new_name = f'spam{new_number:03d}.txt'
                old_path = file
                new_path = folder / new_name

                if old_path.exists():
                    shutil.move(old_path, new_path)
                    existing_numbers.add(new_number)
                    print(f'Renamed {old_path} to {new_path}')
                else:
                    pass

