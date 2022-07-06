# for loop liye toh t(n)=O(n^2) hoga isliye while for O(n)

def search(mat,n,x):
    i=0
    j=n-1
    while (i<n and j>=0):
        if(mat[i][j]==x):
            print("Element found at",i+1,"row and",j+1,"column.")
            return True
        elif (mat[i][j]>x):
            j-=1
        else:
            i+=1
    print("Element not found")
    return False

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 48],
        [32, 33, 39, 50] ]
print(search(mat, 4, 35))
