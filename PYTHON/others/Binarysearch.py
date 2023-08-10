import random

import time

# def naive_search(list, target):

#     for i in range(len(list)):
#         if list[i] == target:
#            return i 
#     return -1

mylist = [1, 3, 5, 10, 12]
# print(naive_search(mylist, 11))

def binary_search(list, target, lower_limit=None, upper_limit=None):

    if lower_limit is None:
        lower_limit = 0
    if upper_limit is None:
        upper_limit = len(list)-1

    if upper_limit < lower_limit:
        return -1
    
    midpoint  = (lower_limit + upper_limit) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, lower_limit, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, upper_limit)


if __name__== '__main__':
  print(binary_search(mylist, 7))