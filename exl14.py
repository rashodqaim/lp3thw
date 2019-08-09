from sys import argv
# script is allways the file name
script, user_name = argv
prompt = '< ' #This shows when asking for input

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # Can also be just ('')
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")

# Argv happen before you run anything and inputs happends as soon as that line of code is written. 