import os
import extension_mapping

def restore(file_name):
    with open("organizer.log", "r") as f:
        lines = f.readline()

    for i in range(len(lines) - 1, -1, -1):

        if lines[i].strip() == f"File: {file_name}":

            info = lines[i + 1].split("|")
            paths = info[1].split("->")

            old_path = paths[0].strip()
            new_path = paths[1].strip()

            if os.path.exists(new_path):
                os.rename(new_path, old_path)
                print("File restored successfully.")
            else:
                print("File not found at the expected location.")

            return

    print("No record found for this file.")

def restore_all():
    with open("organizer.log", "r") as f:
        lines = f.readlines()
    restored = 0
    for i in range(len(lines)-1, -1, -1):
        print(repr(lines[i]))
        if lines[i].startswith("File:"):
            info = lines[i + 1].split("|")
            paths = info[1].split("->")

            old_path = paths[0].strip()
            new_path = paths[1].strip()

            if os.path.exists(new_path):
                os.rename(new_path,old_path)
                restored += 1
    
    print(f"{restored} Files restored successfully.")




            
