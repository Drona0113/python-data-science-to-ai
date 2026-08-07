
from pathlib import Path
import os

def readfileandfolder():
    path=Path(__file__).parent #gives the directory containing this running script
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items.name}") # items.name returns only the final path component instead of full path

      


def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name : ")
        p=Path(__file__).parent/name
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file : ")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exist")
    except Exception as e:
        print(f"An error occured as {e}")


def readfile():
    try:
        readfileandfolder()
        name=input("which file you want to read ? ")
        p=Path(__file__).parent/name
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)

            print("File Read successfully")
        else:
            print("The file do not exist...")
    except Exception as e:
        print(f"An error occured as {e}")


def updatefile():
    try:
        readfileandfolder()
        name=input("tell which file do yu want to update : ")
        p=Path(__file__).parent/name
        if p.exists and p.is_file():
            print("press 1 for changing the name of your file ")
            print("press 2 for overwriting the data of youor file ")
            print("press 3 for appending some content in your file ")
            res=int(input("tell your response : "))

            if res==1:
                name2=input("tell your new file name : ")
                p2=Path(__file__).parent/name2
                p.rename(p2)

            if res==2:
                with open(p,'w') as fs:
                    data=input("tell what you want to write this will overwrite the data : ")
                    fs.write(data)
                    
            if res==3:
                with open(p,'a') as fs:
                                data=input("tell what you want to append : ")
                                fs.write(" "+data)
                                

    except Exception as e:
        print(f"An error occured as {e}")


def deletefile():
    try:
        readfileandfolder()
        name=input("Which file you want to delete : ")
        p=Path(__file__).parent/name
        if p.exists() and p.is_file():
            os.remove(p)

            print("file removed successfully")
        else:
            print("no such file exist")
    except Exception as e:
        print(f"An error occured as {e}")





print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check=int(input("please tell your response: "))

if check==1:
    createfile()
if check==2:
    readfile()

if check==3:
    updatefile()

if check==4:
    deletefile()