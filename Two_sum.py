arr=[1,2,3,4,5,6,78,88,98,35,67,45]
#print(sorted(set(arr))[-2])

# def second_largest(array):
#     k=array[:-1]
#     highest=array[0]
#     second_highest=array[0]
#     for n in array:
#         if n>=highest:
#             highest=n
#         elif n>= second_highest:
#             second_highest=n
#     return second_highest  

# print (second_largest(arr))   
arr=[1,2,3,4,5,6,78,88,98,35,67,45,97]
def two_sum(array,target):
    dict_var={}     # we are storing index of number and difference of number and target , 
    # {99:0, 98:1, 97:2,  .., 12:7, }
    result=[]
    for index,num in enumerate(array):
        if num in dict_var: # in always compares the value with key
            result.append((num,arr[dict_var[num]]))
        dict_var[target-num]=index
    return result   
print(two_sum(arr,target=100))   
        
        
                
            
            
        
            
    