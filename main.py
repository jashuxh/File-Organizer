import os
import time
import extension_mapping
import hashlib
import logger
import restore_point

#TAKES PATH AND PREFERENCE FROM THE USERE:
print("===== File Organizer =====")
user_path = input("Enter path to the Directory:")
os.chdir(user_path)
files = os.listdir()
def is_hidden(file):
    if os.name == "nt":      
        return os.stat(file).st_file_attributes & 2
    else:                    
        return file.startswith(".")
dup_count = 0
print("Choose the number for the service you desire:")
user_input = str(input("1-Organize files.\n2-Scan duplicate files while organizing files.\n3-Restore the files.\n"))
if user_input.lower() == "2":
    warning = str(input("NOTE:-\nThe duplicate files will be transferred to a new folder named 'Duplicate files'\nWant to continue (y/n)"))



    if warning == "y":

    
        
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
                dup_newpath = os.path.join(user_path, "Duplicate files", file )
                dup_oldpath = os.path.join(user_path, file)
                logger.save_dupfile(file,dup_oldpath, dup_newpath)
                dup_count += 1
            else:
                hashes[file_hash] = file

        
count = 0
if user_input == "1" or user_input == "2":
    files = os.listdir()
    print("Processing...")
    time.sleep(3)
    
    for file in files:  #SCANING OF THE NON-DUPLICATE FILES | IT USES "extension_mapping" & "logger.py" FILE:
        
        if is_hidden(file):
            continue
        if os.path.isdir(file):
            continue
        if file == "organizer.log":
            continue
        name, extension = os.path.splitext(file)
        if extension in extension_mapping.images:
            if os.path.isdir("Images") == False:
                os.mkdir("Images")
            os.rename(file , os.path.join("Images", file))
            newpath = os.path.join(user_path, "Images", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)
            

        
        elif extension in extension_mapping.documents:
            if os.path.isdir("Documents") == False:    
                os.mkdir("Documents")
            os.rename(file, os.path.join("Documents", file))
            newpath = os.path.join(user_path, "Documents", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)


        elif extension in extension_mapping.videos:
            if os.path.isdir("Videos") == False:   
                os.mkdir("Videos") 
            os.rename(file , os.path.join("Videos",file))
            newpath = os.path.join(user_path, "Videos", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)

        elif extension in extension_mapping.audio:
            if os.path.isdir("Music") == False:
                os.mkdir("Music")    
            os.rename(file , os.path.join("Music", file))
            newpath = os.path.join(user_path, "Music", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)
            

        elif extension in extension_mapping.archive:
            if os.path.isdir("Archives") == False:  
                os.mkdir("Archives")
            os.rename(file , os.path.join("Archives", file))
            newpath = os.path.join(user_path, "Archives", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)

        elif extension in extension_mapping.no_extention:
            if os.path.isdir("No extention") == False:
                os.mkdir("No extention")
            os.rename(file, os.path.join("No extention", file))
            newpath = os.path.join(user_path, "No extention", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)
        
        else:
            if os.path.isdir("Others") == False:
                os.mkdir("Others")
            os.rename(file, os.path.join("Others",file))
            newpath = os.path.join(user_path, "Others", file )
            oldpath = os.path.join(user_path, file)
            logger.save_file(file,oldpath, newpath)    
        count += 1
if user_input == "3":
    print("Enter the file name to restore it to the old path:")
    file_name = input(">")
    restore_point.restore(file_name)
    
## OUTRO MESSEGE:
if user_input == "2":
    print()
    print("And your duplicate file is transferred differently in a folder.")
    print()
    print(f"Total file Sorted: {count} + {dup_count}(Duplicate files)")
else:
    print()    
    print("Process Done")
    print("Please Check the organized folder in the same path You Entered")
    print()
    print("Total files Sorted:", count)
