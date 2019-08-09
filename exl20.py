#Imports argv from sys
from sys import argv
#Sets argv to be able to add an input
script, input_file = argv

#Funcation call print_all which read whatever file you pass it in the funcation
def print_all(file):
    #print the file that was read
    print(file.read())
#When a file is read it stays on the bottom of a page but this makes it go back to the top
def rewind(f):
    #Tells where to start at
    f.seek(0)
#Funcation that has two arguments
def print_a_line(line_count, f):
    #print the first argument and read the line of the second argument
    print(line_count, f.readline())

#variable called current_file that just opens the input_file
current_file = open(input_file)

print("first lets print the whole file:\n")
#calls funcation with current_file passing through it
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#Calls funcation with current_file passing through it
rewind(current_file)

print("let's print three lines:")

#varaible called current_line equals to 1
current_line = 1 
#Calls funcation and passes current_line and Current_file variables
print_a_line(current_line, current_file) 

#Adds 1 to whatever the current vaule of the current_line is
current_line += 1 #Current line is currently 1 and you add another 1 to it
#calls Funcation passes curent_line and Current_file variables
print_a_line(current_line, current_file) 

#adds 1 to whatever the current vaule of current_line is
current_line += 1 #current line is currently 2 casue we add one in the above funcation and we are now adding 1 more 
#calls funcation passes current_line and Current_file throught it
print_a_line(current_line, current_file)

#you can call the last three funcation with a for loop
#when you call a funcation it set it at that vaule and stops until it you tell it to run again that is why we use loops so we don't have to keep telling it to keep running