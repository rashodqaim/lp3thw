#creates a funcation called cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man thats enough for a party")
    print("Get a blanket.\n")

#prints statement and gives the argments a vaule of 20 and 30
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#prints statement and gives the argments a vaule of varibles 
print("OR, we can use cariables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints statement and gives the argments a vaule after doing the math. The different argments are spreated by a comma
print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#prints statement and gives the argments a vaule of the varaible as well as the number we want added to that varible
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +100)

