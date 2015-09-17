# encoding=UTF-8
__author__ = 'Vincent'

def solve_queen(n):
    queen_pos=[0 for x in range(n)]
    k=1

    while k<n:
        #check the position
        allowed=True
        for i in range(k):
            if queen_pos[k]>=n or queen_pos[i]==queen_pos[k] or abs(i-k)==abs(queen_pos[i]-queen_pos[k]):
                allowed=False
                break
        if allowed:
            #place next queen
            k+=1
        else:
            if queen_pos[k]+1>=n:
                queen_pos[k]=0
                k-=1
            queen_pos[k]+=1
    return queen_pos


print solve_queen(8)