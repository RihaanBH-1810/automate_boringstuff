from pathlib import Path
import re

file = open(Path.cwd()/'filewithdates.txt', 'r')
text = file.read()
file.close()

dates = re.compile(r"((3[01]|[12][0-9]|0?[1-9])[/\-]([1][0-2]|0?[1-9])[/\-]([12]\d{3}))")

m_li = dates.findall(text)

if m_li != None:
    print("I found the following dates in the file: ")
    for i in m_li:
        print(i[0])