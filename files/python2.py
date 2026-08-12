#READ
# print("hello world")

# file = open('study.txt','r')

# re = file.read()

# print(re)

# file.close()

#WRITE
# file = open('notstudy.txt','w')

# file.write("hello nasmaste")

# file.close()


#UPDATE
# file = open('notstudy.txt','a')

# file.write("\n chalo kaam ki bat pe aate ab ye pucho ge ki paise kitne kamate hai....")

# file.close()

#DELETE
# import os

# os.remove("notstudy.txt")

#WRITE ND READ
# fp=open("study.txt","+w")
# fp.write("\nFile handling.")
# content=fp.read()
# print(content)
# fp.close()

#READ ND APPEND
# fp=open("file.txt","+a")
# fp.write("\nLearning python file handling.")
# fp.seek(2)
# content=fp.read()
# print(content)
# fp.close()

#READ ND WRITE
# fp=open("file.txt","+r")
# content=fp.read()
# print(content)
# fp.write("\nFile handling is important.")
# fp.close()


# with open("file.txt","+a") as fp:
#  content=fp.read()
#  print(content)
    
# try:
#   fp=open("file.txt","r")
#   fp.read()
#   fp.close()
# except FileNotFoundError:
#   print("File not found.")


# RENAME FILE

# import os

# os.rename("file.txt", "new_file.txt")


# CHECK FILE EXITS
# import os

# if os.path.exists("new_file.txt"):
#     print("File exists")
# else:
#     print("File does not exist")


# try:
#     file = open('studyiii.txt','r')
#     res = file.read()
#     print(res)
# except FileNotFoundError:
#     print("File not found guys...")

