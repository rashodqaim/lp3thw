# # names = 'hunter,rashod,kyle'
# # list_of_names = names.split(',')
# # count = len(list_of_names)
# # print(count)

# print(len("hunter,Rashod,Kyle".split(',')))
lst = [2, 6, 8, 4, 10]
# def greater_than_five(lst):
#     list_2=[]
#     for number in lst:
#        if isinstance(number, int):
#            if number > 5:
#                 list_2.append(number)
#     return list_2

# print(greater_than_five(lst))

# print(lst)


def odd_numbers_only(lst):
    odds = []
    for num in lst:
        if num % 2 == 1:
            odds.append(num)
    return odds

print(odd_numbers_only(lst))


# nums=[]
# for num in range(0, 10):
#     nums.append(num)

# print(nums)