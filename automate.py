import os
import sys  
import time
import shutil
import subprocess
from datetime import datetime


# File Management with Python
# Every file will be placed at its own directory

class Files:
    
    ext= [".deb", ".jpg", ".tar", ".zip", ".png", "jpeg", ".pdf", ".html",
                ".txt", ".mp4", ".mp3", ".webp", ".py", ".c", ".cpp", ".json", ".js",
                ".css", ".sh", ".bat", ".exe", ".ctx", ".epub", ".docx", ".iso", ".mpp",
                ".pptx", ".xlsx", ".mq5", ".mq4", ".rar", ".appinstaller"]
    
    ms = [".mp3"]
    vd = [".mp4"]
    ps = [".jpg", ".png", "jpeg", ".webp"]
    dc = [".deb", ".tar", ".zip", ".py", ".c", ".cpp", ".json", ".js", ".css", ".sh", ".pdf", ".html", ".bat", ".exe",
          ".ctx", ".txt", ".epub", ".docx", ".iso", ".mpp", ".pptx", ".xlsx", ".mq5", ".mq4", ".rar", ".appinstaller"]

    
    users = os.path.expanduser("~")
    
    paths = []
    pathw = []
    for i in ["Documents", "Videos", "Pictures", "Music"]:
        f = "/".join((users, i))
        w = "\\".join((users, i))
        paths.append(f)
        pathw.append(w)

    def __init__(self):
        pass

    def linux(self):
        if sys.platform.startswith("linux"):
            folder = "Download"
            updated_path = []
            # Let's create a download file in each directory
            for z in self.paths:
                if os.path.exists(f"{z}/{folder}"):
                    folder_path = f"{z}/{folder}"
                    updated_path.append(folder_path)
                    #print("folder {} already exists".format(folder_path))
                else:
                    os.mkdir(f"{z}/Download")
                    #print(f"folder created in: {z}")

            #print(updated_path)       

            current_dir = "Downloads"
            
            all_files = []
            user = os.path.expanduser("~")
            path = "/".join((user, current_dir))
            dst = "/".join((user, self.paths[-1]))
            for n, i in enumerate(os.listdir(path)):
                for j in self.ext:
                    if i.endswith(j):
                        all_files.append(i)
                        
            
                        #Here we are moving into the documents/download folder
                        try:
                            for k in self.dc:
                                if k in i:
                                    
                                    # What if there's a file code.deb in downloads and documents/donwload
                                    try:
                                        shutil.move(f"{path}/{i}", updated_path[0]) # Or its either here
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming, ext = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming) # here you can replace the naming with ext
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{k}"
                                        os.rename(f"{path}/{i}", f"{path}/{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}/{new_name}", updated_path[0]) # I think the problem is here

                            # Here we are moving into the pictures/download folder
                            for r in self.ps:
                                if r in i:
                                    
                                    try:
                                        shutil.move(f"{path}/{i}", updated_path[2])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{r}"
                                        os.rename(f"{path}/{i}", f"{path}/{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}/{new_name}", updated_path[2])
                                
                            # Here we are moving into the music/download folder
                            for m in self.ms:
                                if m in i:
                                    
                                    try:
                                        shutil.move(f"{path}/{i}", updated_path[3])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{m}"
                                        os.rename(f"{path}/{i}", f"{path}/{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}/{new_name}", updated_path[3])            
                                
                            # Here we are moving into the video/download folder
                            for t in self.vd:
                                if t in i:
                                    
                                    # Why is it printing that files not found
                                    try:
                                       shutil.move(f"{path}/{i}", updated_path[1])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                        else:
                                            file_name = naming[0]

                                        new_name = f"{file_name}_{times}{t}"
                                        os.rename(f"{path}/{i}", f"{path}/{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                        
                                            shutil.move(f"{path}/{new_name}", updated_path[1])

                            
                                    
                        except FileNotFoundError as e:
                            print(e)
            # What if the directoy is empty
            print("file moved successfully :)")
        # else:
        #     print(f"Not supported in {sys.platform}")



    def windows(self):
        if sys.platform.startswith("win32"):
            folder = "Download"
            updated_path = []
            # Let's create a download file in each directory
            for z in self.pathw:
                if os.path.exists(f"{z}//{folder}"):
                    folder_path = f"{z}//{folder}"
                    updated_path.append(folder_path)
                    #print("folder {} already exists".format(folder_path))
                else:
                    os.mkdir(f"{z}//Download")
                    #print(f"folder created in: {z}")

            #print(updated_path)       

            current_dir = "Downloads"
            
            all_files = []
            user = os.path.expanduser("~")
            path = "//".join((user, current_dir))
            for n, i in enumerate(os.listdir(path)):
                for j in self.ext:
                    if i.endswith(j):
                        all_files.append(i)

                        #Here we are moving into the documents/download folder
                        try:
                            for k in self.dc:
                                if k in i:
                                    
                                    # What if there's a file code.deb in downloads and documents/donwload
                                    try:
                                        shutil.move(f"{path}\\{i}", updated_path[0]) # Or its either here
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{k}"
                                        os.rename(f"{path}\\{i}", f"{path}\\{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}\\{new_name}", updated_path[0]) # I think the problem is here

                            # Here we are moving into the pictures/download folder
                            for r in self.ps:
                                if r in i:
                                    
                                    try:
                                        shutil.move(f"{path}\\{i}", updated_path[2])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{r}"
                                        os.rename(f"{path}\\{i}", f"{path}\\{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}\\{new_name}", updated_path[2])
                                
                            # Here we are moving into the music/download folder
                            for m in self.ms:
                                if m in i:
                                    
                                    try:
                                        shutil.move(f"{path}\\{i}", updated_path[3])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                            
                                        else:
                                            file_name = naming[0]
                                        new_name = f"{file_name}_{times}{m}"
                                        os.rename(f"{path}\\{i}", f"{path}\\{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                            shutil.move(f"{path}\\{new_name}", updated_path[3])            
                                
                            # Here we are moving into the video/download folder
                            for t in self.vd:
                                if t in i:
                                    
                                    # Why is it printing that files not found
                                    try:
                                       shutil.move(f"{path}\\{i}", updated_path[1])
                                        
                                    except shutil.Error:
                                        # example pf how it will look like code_1.deb, code_2.deb
                                        now = datetime.now()
                                        times = now.strftime("%d-%m-%Y-%H-%M") 
                                        naming = i.split(".")
                                        if len(naming) > 2:
                                            nm = naming.pop()
                                            file_name = " ".join(x for x in naming)
                                        else:
                                            file_name = naming[0]

                                        new_name = f"{file_name}_{times}{t}"
                                        os.rename(f"{path}\\{i}", f"{path}\\{new_name}")
                                         # the only problem is the shutil.move is moving a file that doesn't exist
                                        # how are we going to say that once renaimed move it?
                                        if new_name in os.listdir(path):
                                            print(new_name)
                                        
                                            shutil.move(f"{path}\\{new_name}", updated_path[1])

                            
                                    
                        except FileNotFoundError as e:
                            print(e)
            # What if the directoy is empty
            print("file moved successfully :)")

if __name__ == '__main__':
    file = Files()
    file.windows()
    file.linux()

# run the following command: python file_name.py install