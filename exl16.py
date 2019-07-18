# import argv
from sys import argv
# have a filename equal to argv, the file name can be any file you want or create
script, filename = argv
# print line with filrname that was created
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# add an input
input("?")

print("Opening the file...")
# variable called target opens filename from above
target = open(filename, 'w')

print("Truncation the file. Goodbye!")
# truncate mean to erase the file
target.truncate()

print("Now I'm going to ask you for three lines.")
# 3 different variables asking for a input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# variable target is writing anything and saving it.
target.write(line1 + '\n' + line2 +'\n' + line3 + '\n')
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
# closes file
target.close()
