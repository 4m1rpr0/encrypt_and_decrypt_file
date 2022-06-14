import os

path_file = input("Enter The File Path : ")

if os.path.exists(path_file):
    with open(path_file, "rb") as file:
        with open(os.getcwd() + "/encrypt", "wb") as file1:
            for i in file.read():
                i = i ^ ord("b")
                file1.write(i.to_bytes(1, "big"))
    print("success")
else:
    print("error")