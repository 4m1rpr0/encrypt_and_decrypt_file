import os
def crypto(path, check):
    if os.path.exists(path):
        with open(path, "rb") as file:
            with open(os.getcwd() + "/" + check, "wb") as file1:
                for i in file.read():
                    i = i ^ ord("b")
                    file1.write(i.to_bytes(1, "big"))
        print("success")
    else:
        print("error")
print("Started Program\n1 - Encrypt File\n2 - Decrypt File\n3 - Exit")
while True:
    check = input(">>> ")
    if check == "1":
        crypto(input("Enter The File Path (Encrypt File): "), "Encrypt")
    elif check == "2":
        crypto(input("Enter The File Path (Decrypt File) : "), "Decrypt")
    elif check == "3":
        print("bye :)")
        break
    else:
        print("error")