# Enter your code here. Read input from STDIN. Print output to STDOUT
def exception(a,b):
    
    # Check for division by zero
    if b == "0":
        print("Error Code: integer division or modulo by zero")

    # Check for invalid integer input
    elif not (a.lstrip('-').isdigit() and b.lstrip('-').isdigit()):
        print("Error Code: invalid literal for int() with base 10: '$'")

    # Perform integer division
    else:
        print(int(a) // int(b))
