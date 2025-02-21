import os
import shutil


path = r'<path to files to be sorted>'

# Make new folders to sort the files into
folder_names = ['CSV Files', 'Text Files', 'Image Files']

for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# List the files in the directory
file_names = os.listdir(path)

# Move the files into the corresponding directories
for file in file_names:
    if ".csv" in file and not os.path.exists(path + "CSV Files\\" + file):
        shutil.move(path + file, path + "CSV Files\\" + file)
    elif ".png" in file and not os.path.exists(path + "Image Files\\" + file):
        shutil.move(path + file, path + "Image Files\\" + file)
    elif ".txt" in file and not os.path.exists(path + "Text Files\\" + file):
        shutil.move(path + file, path + "Text Files\\" + file)