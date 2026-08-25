#hashing_first_unique element
nums = [4, 5, 1, 2, 1, 5, 4, 7, 2]
def first_unique(nums):
    unique={}
    for num in nums:
        unique[num]=unique.get(num,0)+1
    for num in nums:
        if unique[num] == 1:
            return num

    return(num)

print(first_unique(nums))