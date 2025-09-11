with open('d2.txt', 'w+') as file:
    content = file.write("\n Hi there, welcome to file handling part 2")
    file.seek(0)
    see = file.read()

    print(content)
 
"""    print(see)
with open('image.png', 'rb') as file:
    data = file.read()
    # Process the binary data
"""
#reading a csv file
import csv
import io

# Create a CSV sample in memory
# csv_data = """Year,Industry,Value
# 2014,Manufacturing,769400
# 2014,Manufacturing,48000
# 2014,Manufacturing,12
# """
# csvfile = io.StringIO(csv_data)
# csvreader = csv.reader(csvfile)
# for row in csvreader:
#     print(row)
# """Instead of a physical file, we used StringIO to create a file-like object. 
# The CSV reader parses each line into a list of values."""
# #reading json file
# import json
# with open("sample1.json", "r") as jsonfile:
#     data = json.load(jsonfile)
#     print(data)
#more example
with open("d.txt", "w", encoding="utf-8") as file:
    file.write("File Handling\n")
    file.write("Python is so much fun\n")
    file.write("i love coding\n")
    file.write("Yayyy, done. \n")
with open("d.txt", "r", encoding="utf-8") as file:
    print(file.read())
with open("d.txt", "a", encoding="utf-8") as file:
    file.write("Appended line.\n")

with open("d.txt", "r", encoding="utf-8") as file:
    print(file.read())
    #exclusive x and errir handline
try:
    with open("d.txt", "x", encoding="utf-8") as file:
        file.write("Created using exclusive mode.\n")
except FileExistsError:
    print("d.txt already exists, exclusive creation aborted.")
#write mutiple lines
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("file1.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as f:
    print(f.read())