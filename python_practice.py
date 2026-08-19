
    # Given an array of integers nums, find the element that appears most frequently.
    # If there are multiple elements with the same maximum frequency, return the smallest one.
def max_freq(nums):  
    dict_num = {}
    for i in nums:
        if i in dict_num:
            dict_num[i] += 1
        else:
            dict_num[i] = 1
    values_max= max(dict_num.values())
    for j in dict_num:
        if dict_num[j]==values_max:
            max_key=j
    return (max_key)
    
#nums = [1, 3, 2, 3, 1, 1, 4, 2, 2, 2]
# print(max_freq(nums))
fruit_name= "mango"
fruits_tup = (('banana',6), ('orange',8), ('mango',9), ('guava',20), ('grapes',45))
def get_fruit_count(fruit_name,fruits_tup):
    fruits_dict=dict(fruits_tup)
    return fruits_dict[fruit_name]
    # for fruit in fruits_tup:
    #      in_fruit,num = fruit
    #      if fruit_name==in_fruit:
    #         return num
    
        
# result= get_fruit_count(fruit_name,fruits_tup)
# # print(result)       
            
def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    return fact
# print(factorial(5))

def cal_factorial(num):
    """It is a recussive approach, time and space both is O(n) """
    if num<=1:
        return 1
    else:
        return num*cal_factorial(num-1)
# print(cal_factorial(5))

from functools import reduce
lst=[1,2,3,4,5,6]
lst_squared=reduce(lambda x,y: x+y,lst)

print(lst_squared)




