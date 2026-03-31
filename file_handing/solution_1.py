from pathlib import Path

def readfileandfolder():
    path = Path('')
    item = list(path.rglob('*'))
    for i, item in enumerate(item):
        print (f"{i+1}: {item}")
        
        
def createfile():
    try:
        readfileandfolder()
        filename = input("enter the file name you want to create: ")
        p = Path(filename)
        if not p.exists():
            with p.open(mode='w') as fs:
                        data = input("enter the data you want to write in file: ")
                        fs.write(data)
            print(f"File created successfully")
            
        else:
            print("file already exists")
            
    except Exception as e:
        print (f"AN error occurred: {e}")


def readfile():
    try:
        readfileandfolder()
        filename = input("enter the file name you want to read: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            with p.open(mode='r') as fs:
                data = fs.read()
                print(f"File contents:\n{data}")
        else:
            print("File not found")
            
    except Exception as e:
        print (f"AN error occurred: {e}")


def updatefile():
    try:
        readfileandfolder()
        filename = input("enter the file name you want to update: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            print("press 1 for changing the file name")
            print("press 2 for overwriting thedata in file")
            print("press 3 for appending the data in file")
            option = int(input("enter your option: "))
            if option == 1:
                new_filename = input("enter the new file name: ")
                new_p = Path(new_filename)
                if not new_p.exists():
                    p.rename(new_p)
                    print(f"File renamed successfully to {new_filename}")
                else:
                    print("File with the new name already exists")
            elif option == 2:
                with p.open(mode='w') as fs:
                    data = input("enter the data you want to overwrite in file: ")
                    fs.write(data)
                print(f"File overwritten successfully")
            elif option == 3:
                with p.open(mode='a') as fs:
                    data = input("enter the data you want to append in file: ")
                    fs.write(data)
                print(f"File updated successfully")
        else:
            print("File not found")
            
    except Exception as e:
        print (f"AN error occurred: {e}")


def deletefile():
    try:
        readfileandfolder()
        filename = input("enter the file name you want to delete: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"File deleted successfully")
        else:
            print("File not found")
            
    except Exception as e:
        print (f"AN error occurred: {e}")

while True:
    print ("print 1 for create a file")
    print ("print 2 for update a file")
    print ("print 3 for read a file")
    print ("print 4 for delete a file")
    print ("print 5 for exit")

    option = int(input("enter your option: "))


    if option == 1:
        createfile()


    if option == 2:
        readfile()
        

    if option == 3:
        updatefile()
        
    if option == 4:
        deletefile()
        
    if option == 5:
        print("exiting the program")
        break