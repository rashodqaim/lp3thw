from sys import argv
#read the WYSS section fro how to fun this
script, first, second, third, Thai, Mexican, Dinner = argv

print("the script is called:", script)
print("your first variable is:", first)
print("Your second varibale is:", second)
print("Your third variable is:", third)
lunch = input("What do you want to eat")
# I can replace the argv with anything I want when I run it in the terminal
print(f"V1 {first}, V2 {second}, V3 {third}")


# Dinner, Thai, Mexican = argv
print("the script is called:", Dinner)
print("your first variable is:", Thai)
print("Your second varibale is:", Mexican)
print(f"Yes we can have {lunch} for lunch today")

#Notes What ever the order the argv is in that is the order I have to write it in the terminal.
