# We are unpacking the args in this funcation but this is not necearry there is an easier way to write this
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#This is the best way to write the funcation
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")
#We just need one argument to call this funcation
def print_one(arg1):
    print(f"arg1: {arg1}")
#We dont need any arguments to call this funcation
def print_none():
    print("I got nothing'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()