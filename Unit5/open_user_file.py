'''
Create a program that takes a filename from the user and tries to open the file for reading and handle these exceptions and provide appropriate error messages for following cases.
1.1) FileNotFoundError: If the file does not exist.
2.2) PermissionError: If the program lacks permissions to read the file.
'''

path = input("Enter file's path: ")

try:
    with open (path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print(f"{error} occured!")
except PermissionError as error:
    print(f"{error} occured!")