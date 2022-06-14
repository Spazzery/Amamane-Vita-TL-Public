# Amamane-Vita-TL-Public
Tools and scripts I used for Amamane's English MTL

Currently, there are 2 tools included in this repository:
extract text fixed.py and insert text.py

To extract Japanese text from the game's lua files, you need to run the extract text fixed.py. It will look for lua scripts in the same directory where the .py files are. And it will place the extracted texts into a folder called "Extracted". Note: you need to provide the Japanese lua scripts yourself.

To insert translated lines into Vita's lua scripts, you need to have the translated txt files in the same directory as the .py files and lua scripts. Then run insert text.py. It will insert text from your translated txt files into the lua files and put them in a folder "Translated Lua Scripts".

Almost every lua script also has a text in the beginning denoting the chapters name. These I changed manually.
For example, for ama_01.lua, the chapter's name is "The birth of "Amamane"!".


As for the translation, I manually copy-pasted the Japanese texts from Extracted/* to DeepL and then pasted the result into the files. I did create another small tool using DeepL's Python API, but I felt it did a worse job, because it was translating each line individually without the context of other lines, which the DeepL web app does to my knowledge.
