import os
import shutil

def organize_files(directory):
    file_types={
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".pdf", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Others": []  
    }

    for catagory in file_types:
        catagory_dir=os.path.join(directory, catagory)
        os.makedirs(catagory_dir,exist_ok=True)
    
    for filename in os.listdir(directory):
        file_path=os.path.join(directory,filename)
        if os.path.isfile(file_path):
            file_ext=os.path.splitext(filename[1].lower)
            moved=False
            for catagory, extentions in file_types.items():
                if file_ext in extentions:
                    destination_dir= os.path.join(directory,catagory)
                    shutil.move(file_path, os.path.join(destination_dir ,filename))
                    print(f"Moved{filename} to {catagory} folder")
                    moved=True
                    break
            if not moved:
                destination_dir=os.path.join(directory, 'Other')
                shutil.move(file_path, os.path.join(destination_dir,filename))
                print(f"Moved{filename} to other folder")
    print("Organizing Completed")

        

def main():
    directory=input("Enter the path of the directory")
    if os.path.exists(directory) and os.path.isdir(directory):
        organize_files(directory)
    else:
        print("Invalid directory  path. Please provide a valid path")

if __name__=="__main__":
    main()
