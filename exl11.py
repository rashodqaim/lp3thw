# Print statement when you have the word "end" at the end of the statement, the program doesn't go to the next time but still runs the code
print("How old are you?", end='')
#variable called age where it ask for the input which could be anything
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = int(input())
#print statement with all the variable inputs
print(f"So, you're {age} old, {height} tall and {weight} heavy.")


print("What is your favorite animal?", end='')
animal = input()
print("How many pets do you have?", end='')
pets = input()
print("Enter your name")
name = input()
print(f"Your favorite animal is {animal}, you have {pets} pets, and your name is {name}")
