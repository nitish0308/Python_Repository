a= (3,4)
b= (1,2)
product=[]
def car_p(a,b):
    for i in a:
        for y in b:
            product.append((i,y))
    product.sort()       
    print(","product)        

    return()

car_p(a,b)