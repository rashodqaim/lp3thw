#Funcation that returns whatever vaule you put in for a & b
def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b


print("let's do some math with just funcations!")
# You can call a funcation inside a variable
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")



print("Here is a puzzle.")
# does the math in the terminal to show you what it was doing
what = add(age, subtract(height, multiply(weight,divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand")

#Doing the math yourself and making it much easier to read also
def puzzle(a):
    iq2 = iq/a
    weight2 = weight * iq2 
    height2 = height - weight2 
    age2 = age + height2
    return age2, iq2


print(puzzle(2))
