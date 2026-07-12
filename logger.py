import time


def save_dupfile(file,oldpath,newpath):
    with open("organizer.log", "a") as f:
        f.write(f"Duplicate File: {file}\n")
        f.write(f"{time.ctime()} | {oldpath} -> {newpath}\n")

def save_file(file,oldpath,newpath):
    with open("organizer.log", "a") as i:
        i.write(f"File: {file}\n")
        i.write(f"{time.ctime()} | {oldpath} -> {newpath}\n")


