import os
import re

save_path = './Translated Lua Scripts'
dir = os.path.join("Translated Lua Scripts")

if not os.path.exists(dir):
    os.mkdir(dir)


def english_text_to_list(filename):
    filename_txt = filename[:-4] + ".txt"
    for txt_file in os.listdir():
        if txt_file == filename_txt:
            openFile = open(txt_file, "r", encoding="utf-8")
            data = openFile.read()
            return data.split("\n")


def replace_japanese_text_with_english(filename):
    completename = os.path.join(save_path, filename)

    english_text_list = english_text_to_list(filename)
    lua_file = open(filename, "r+", encoding="utf-8")
    lua_file_data = lua_file.read()
    lua_file.close()

    translated_lua_file_data = lua_file_data
    count = 0
    for match in re.finditer("(\[\"text\"]) = ({\[\[(.*)]]})", lua_file_data):
        english_sentence = english_text_list[count]

        # If Japanese source sentence has Japanese quotation marks, and the English sentence doesnt have them, add them
        if match.group(3).startswith("「") and english_sentence[0] != "\"":
            english_sentence = "\"" + english_sentence
        if match.group(3).endswith("」") and english_sentence[-1] != "\"":
            english_sentence = english_sentence + "\""

        translated_lua_file_data = translated_lua_file_data.replace(match.group(3), english_sentence, 1)
        count += 1

    createfile = open(completename, "w", encoding="utf-8")
    createfile.write(translated_lua_file_data)
    createfile.close()


for filename in os.listdir():
    if filename.endswith('.lua'):
    # if filename == "ama_01.lua":
        replace_japanese_text_with_english(filename)
