import os
import os.path
# import pathlib    #OR

'''
Write a program which prints the full path for all files in the current directory, one per line. Use either the os module or pathlib.

Write a program which copies a file from a source, to a destination without using shutil, or the OS copy command. You are essentially writing a simple version of the OS copy command.

    This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') or 'wb' for writing. Note that for binary files you can’t use readline(). Lines don’t have any meaning for binary files.

    Test it with both text and binary files. Maybe a jpeg or something of your choosing.

    Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.

    This should only be a few lines of code.
'''
# Program 1
cwd = os.getcwd()
print(cwd)
for each in os.listdir(cwd):
    print(os.path.abspath(each))

# Program 2
# with open("pic.png", "rb") as p1_in, open("copy_pic.png", "wb") as p1_out:
with open("students.txt", "rb") as p1_in, open("copy.txt", "wb") as p1_out:
    for i in range(10):
        p1_out.write(p1_in.readline())
print(p1_in.closed)
print(p1_out.closed)