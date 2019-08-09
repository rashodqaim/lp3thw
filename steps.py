# read file name.txt
# if file has a name in it, print "Hello <name>"
# if file doesn't have a name in it, ask the user for their name
# store their name in name.txt
# print "Hello <name>"

# the first time this program is run, it should prompt the user for their name and then greet them
# every subsequent time the program runs, it should just greet them

# from sys import argv 
# script, filename = argv

# open_file = open("filename", 'w')

# def foo(bar):
#     if filename.read():
#         print(f"Hello {filename}")

#     else:
#         print("What is your name?")
#         new_name =input()
#         print(f"Hello {new_name}")

# foo("Rashod")

#open file done
#read File done
#print the file done 
# filename ="name.txt"
# open_file = open(filename)
# read_file = open_file.read()
# print(read_file)

# Write in file Done
# filename ="name.txt"
# open_file = open(filename, 'w')
# open_file.write("Qaim")

#input from the user Done
# ask = input("What is your name")
# print(f"Hello {ask}") 


#check if file is empty Done
# import os
# filename ="name.txt"
# open_file = open(filename)
# read_file = open_file.read()
# check = os.stat(filename).st_size == 0
# print(check)





import os

filename ="name.txt"
open_file = open(filename)
read_file = open_file.read()

empty = os.stat(filename).st_size == 0

if not empty:
    name = read_file

else:
    name = input("What is your name ")
    open_file = open(filename, 'w')
    open_file.write(name)
    

print(f"Hello {name}")

