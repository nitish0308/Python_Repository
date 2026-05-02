def permutation(mylist,r):
#mylist is string and r is  length of the iterable.
    y = list(itertools.permutations(task1, per_no)) 
    y.sort()
    for i in y:
        print(''.join(i))