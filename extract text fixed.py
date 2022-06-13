import os
import re

save_path = './Extracted'
dir = os.path.join("Extracted")

if not os.path.exists(dir):
    os.mkdir(dir)

def extract(filename):
    my_list = []
    filename_txt = filename[:-4] + ".txt"
    completename = os.path.join(save_path, filename_txt)
    openFile = open(filename, "r+", encoding="utf-8")
    data = openFile.read()
    for match in re.finditer("(\[\"text\"]) = ({\[\[(.*)]]})", data):
        my_list.append(match.group(3))
    openFile.close()

    createfile = open(completename, "w", encoding="utf-8")
    for i in my_list:
        createfile.write(i)
        if not i == my_list[-1]:
            createfile.write("\n")
    createfile.close()


for filename in os.listdir():
    if filename.endswith('.lua'):
        extract(filename)