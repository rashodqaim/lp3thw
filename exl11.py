# Print statement but when a end='' at the end of line, this tells print to end the line with a newline character and go to the input
print("How old are you?", end='') #its going to ask you to put in a input 
#variable called age where it ask for the input of the line above
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()
#print statement with all the variable inputs
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
