# Expected Time Complexity:O(N^2LogN)
# Expected Auxillary Space:O(N^2)

def sortMat(mat, n) :
    temp = [0] * (n * n)
    k = 0
    for i in range(0, n) :
        for j in range(0, n) :
            temp[k] = mat[i][j]
            k += 1
    temp.sort()
    k = 0
    for i in range(0, n) :
        for j in range(0, n) :
            mat[i][j] = temp[k]
            k += 1
def printMat(mat, n) :
    for i in range(0, n) :
        for j in range( 0, n ) :
            print(mat[i][j] , end = " ")
        print()

# Driver program to test above
mat = [ [10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50] ]
n = 4

print( "Original Matrix:")
printMat(mat, n)
sortMat(mat, n)
print("\nMatrix After Sorting:")
printMat(mat, n)

x=39
for i in range(n):
    for j in range(n):
        if mat[i][j]==x:
            print("Position found at",i+1,"row and column is",j+1)