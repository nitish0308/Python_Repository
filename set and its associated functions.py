

def apply_operation(s, command):
    parts = command.split()
    func_name = parts[0]
    args = list(map(int, parts[1:]))

    # Get the set method dynamically
    m = getattr(s, func_name)

    # Call the method with unpacked arguments
    m(*args)


# Main program
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input()
    apply_operation(s, command)

print(sum(s))