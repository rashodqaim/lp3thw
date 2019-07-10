# variable that has 4 brackets to add data points in
formatter = "{} {} {} {}"

# print the variable with all these data points, these are ints
print(formatter.format(1, 2, 3, 4))
# print the variable with all these data points, these are strings
print(formatter.format("one", "two", "three", "four"))
# print the variable with all these data points, these are bloons
print(formatter.format(True, False, False, True))
# print the variable will all the other data points being variables
print(formatter.format(formatter, formatter, formatter, formatter))
# # print the variable with all these data points, these are strings also but easier to read
print(formatter.format(
    "Try your",
    "Own text here",
    "maybe a poem",
    "Or a song about fear"
))



print( "mary had a little lamb")
print ("and her fleece was as white as {}".format("snow"))
print ("everywhere that mary went.")
print("." * 10)
