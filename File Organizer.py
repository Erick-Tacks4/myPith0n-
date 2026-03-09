import os
import shutil

folder = input("Enter the folder path:  ")

for filename in os.listdir(folder):
    name, ext = os.path.splitext(filename)
    ext = ext[1:] #Remove the dot

    if ext == "":
        continue
    ext_folder = os.path.join(folder, ext.upper() + "_files")
    if not os.path.exists(ext_folder):
        os.mkdir(ext_folder)

    shutil.move(os.path.join(folder, filename), os.path.join(ext_folder, filename))    

print("Files Organized by type")