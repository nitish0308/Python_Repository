
def average(array):
    # your code goes here
    arr_len=len(set(array))
    set_arr=set(array)
    sum_arr=0
    for i in set_arr:
        sum_arr=sum_arr+int(i)
    average_arr=sum_arr/arr_len    
    return(average_arr)