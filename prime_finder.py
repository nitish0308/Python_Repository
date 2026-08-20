   # To write a concise Python prime number checker using the built-in all() function alongside def, if, else, and for, define a function that evaluates whether any integer up to the square root evenly divides the input
def prime_finder(lst):
    final_lst=[]
    for num in lst:
        if num<2:
            pass
            #print(f'{num}:is not prime number')
        elif num==2:
            
            #print(f'{num}:is prime number')
            final_lst.append(num)
        elif all(num%x!=0 for x in range(2,num) ):
            final_lst.append(num)
            #print((f'{num}:is not prime number'))
        else: 
            pass
    print(f'{final_lst}:are prime numbers')
    return final_lst

# #other method
# def prime_finder1(lst):
#     for n in lst:
#         if n < 2:
#             print(n, "Not Prime")
#         else:
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     print(n, "Not Prime")
#                     break
#             else:
#                 print(n, "Prime")
         
         
         
# #lst=[1,2,3,4,5,6,7,8,9,0,23,4,67,89,45,65,77,89,34]   
# prime_finder(lst)
                
                
                   