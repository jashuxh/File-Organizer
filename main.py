import os
import time
import extension_mapping
import hashlib

user_path = input("Enter path to the Directory:")
os.chdir(user_path)
files = os.listdir()
user_input = input("Want to check duplicate files?: (y/n)")

if user_input.lower() == "y":
    warning = input("NOTE:-\nThe duplicate files will be transferred to a new folder named 'Duplicate files'\nWant to continue (y/n)")

def is_hidden(file):
    if os.name == "nt":      
        return os.stat(file).st_file_attributes & 2
    else:                    
        return file.startswith(".")
dup_count = 0
if warning.lower() == "y":
    
    hashes = {}
    
    for file in files:
        
        if is_hidden(file):
            continue

        if os.path.isdir(file):
            continue

        with open(file, "rb") as f:
            data = f.read()
            file_hash = hashlib.sha256(data).hexdigest()
        
        if file_hash in hashes:
            if os.path.isdir("Duplicate files") == False:
                os.mkdir("Duplicate files")
            os.rename(file, os.path.join("Duplicate files", file))
        
        else:
            hashes[file_hash] = file
        dup_count += 1
files = os.listdir()
print("Processing...")
time.sleep(3)
count = 0
for file in files:
    

    if is_hidden(file):
        continue
    if os.path.isdir(file):
        continue
    name, extension = os.path.splitext(file)
    if extension in extension_mapping.images:
        if os.path.isdir("Images") == False:
            os.mkdir("Images")
        os.rename(file , os.path.join("Images", file))

    
    elif extension in extension_mapping.documents:
        if os.path.isdir("Documents") == False:    
            os.mkdir("Documents")
        os.rename(file, os.path.join("Documents", file))


    elif extension in extension_mapping.videos:
        if os.path.isdir("Videos") == False:   
            os.mkdir("Videos") 
        os.rename(file , os.path.join("Videos",file))

    elif extension in extension_mapping.audio:
        if os.path.isdir("Music") == False:
            os.mkdir("Music")    
        os.rename(file , os.path.join("Music", file))

    elif extension in extension_mapping.archive:
        if os.path.isdir("Archives") == False:  
            os.mkdir("Archives")
        os.rename(file , os.path.join("Archives", file))

    elif extension in extension_mapping.no_extention:
        if os.path.isdir("No extention") == False:
            os.mkdir("No extention")
        os.rename(file, os.path.join("No extention", file))
    else:
        if os.path.isdir("Others") == False:
            os.mkdir("Others")
        os.rename(file, os.path.join("Others",file))    
    count += 1
print()    
print("Process Done")
print("Please Check the organized folder in the same path You Entered")
print()
print("Total files Sorted:", count)
if warning.lower() == "y":
    print()
    print("And your duplicate file is transferred differently in a folder.")
    print()
    print("Total file Sorted:", count," + ", "(Duplicate files)")
