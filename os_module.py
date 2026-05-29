import os

# print(os.getcwd()) # Print current directory

# os.chdir("D:/gaurang/Python/os_module/demo") # For change directory
# print(os.getcwd())

# os.mkdir("class") # create directory
# print("Directory created")

# print("Files are:",os.listdir()) # list of directory

# print(os.path.abspath("sample.txt")) # To check absolute path

# print(os.path.isdir("sample.txt")) # check file or folder is present in directory
# print(os.path.isdir("demo"))

# os.rename("demo","test") # Rename folder
# os.chdir("test/class")
# os.rename("sample.txt","test.txt") # Rename file

os.chdir("test")
print("current dir is :",os.getcwd())
os.rmdir("class")

