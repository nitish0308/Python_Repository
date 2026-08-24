#Hashing_Two_sum

nums = [2, 71, 11, 15, 13, 6]
target = 9
def two_sum(nums, target):
    dict_var={}
    for i,num in enumerate(nums):
        complement= target-num 
        
        if complement in dict_var:
            return [complement, num]
        
        dict_var[num] = i

    return []

print(two_sum(nums, target))


