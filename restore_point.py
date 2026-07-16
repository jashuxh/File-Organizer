import os

def restore(file_name):
    with open("organizer.log", "r") as f:
        lines = f.readlines()

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

            
