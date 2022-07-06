# T(n)=O(r*c)       S(n)=O(1) for returning answer

def spiralprint(r,c,a):
    k=0                                #startingrowindex
    l=0                                #startingcolurnindex
    #r=endingrowindex     n=endingcolurnindex
    while (k<r and l<c):
        for i in range(l,c):
            print(a[k][i],end=' ')
        k+=1
        for i in range(k,r):
            print(a[i][c-1],end=' ')
        c-=1
        if(k<r):
            for i in range(c-1,(l-1),-1):
                print(a[r-1][i],end=' ')
            r-=1
        if(l<c):
            for i in range(r - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1

a=[[ 1, 2, 3 ],[ 5, 6, 7 ],[ 9, 10, 11 ],[ 13, 14, 15 ]]
r=4
c=3
spiralprint(r,c,a)