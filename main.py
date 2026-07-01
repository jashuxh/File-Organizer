import os
import time
import extension_mapping


user_path = input("Enter path to the Directory:")
os.chdir(user_path)
files = os.listdir()
print("Processing...")
time.sleep(3)



for file in files:
    name, extension = os.path.splitext(file)
    print(extension)
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

    else:
        if os.path.isdir("Others") == False:
            os.mkdir("Others")
        os.rename(file, os.path.join("Others",file))
    
print("Process Done")
print("Please Check the organized folder in the same path,\nYou Entered")

