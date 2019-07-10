from collections import defaultdict
d = defaultdict(list)

n, m = map(int,input().split())

def find_occurences(n,m):
    '''
    find the index number of the letter in the
    first group and print the index positions
    '''
    for i in range(n):
        grpA = input()
        d[grpA].append(str(i+1))
    for j in range(m):
        grpA = input()
        print(" ".join(d[grpA]) or -1) 

find_occurences(n,m)