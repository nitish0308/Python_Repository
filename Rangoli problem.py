def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    width = 4 * size - 3


    for i in range(size - 1, -size, -1):
        x = abs(i)

        left = alphabet[size-1:x:-1]
        right = alphabet[x:size]

        row = "-".join(left + right)

        print(row.center(width, "-"))


n = int(input())
print_rangoli(n)