# Import argv
from sys import argv
# have a argv equal to variable filename
script, filename = argv
# Open a file, candy is a variable
candy = open(filename)

print(f"Here's your file {filename}:")
#print the variable candy after reading file
print(candy.read())
candy.close()
#print line
print("type the filename again:")
# variable called file_again and it asked for an input
file_again = input("> ")
#Open variable file_again and equal to variable txt_again
txt_again = open(file_again)
# print txt_again after reading file
print(txt_again.read())
txt_again.close()
