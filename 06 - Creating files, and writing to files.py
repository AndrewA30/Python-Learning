import os

path = "D:\Python Learning"
#before create new file, check the existing file name
# dir_list = os.listdir(path)
# print("List of directories and files before creation:")
# print(dir_list)

#create file (w):Open the file for writing. For an existing file, the data is truncated and over-written.  (a): Open the file for writing. The data being written will be inserted at the end, after the existing data.
# with open("filetesting.txt","w") as fp:
#     pass;

# write text to the files
file1 = open("filetesting.txt","a")

L = ["This is Medan \n", "This is Jakarta \n", "This is Batam \n"]

file1.writelines(L)

file1.close()