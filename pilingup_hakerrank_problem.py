from collections import deque

for _ in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    
    last = float('inf')   # previous picked cube (start with infinity)
    
    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()
        
        if pick <= last:
            last = pick
        else:
            print("No")
            break
    else:
        print("Yes")