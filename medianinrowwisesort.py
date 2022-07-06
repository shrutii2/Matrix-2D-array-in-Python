'''
Time Complexity: O(32 * r * log(c)). 
The upper bound function will take log(c) time and is performed for each row. 
And since the numbers will be max of 32 bit, so binary search of numbers from min to max will be performed in at most 32 ( log2(2^32) = 32 ) operations. 
Auxiliary Space: O(1) 
'''

from bisect import bisect_right as upper_bound

def binaryMedian(mat, r, c):
    mini = mat[0][0]
    maxi = 0
    for i in range(r):
        if mat[i][0] < mini:
            mini = mat[i][0]
        if mat[i][c-1] > maxi :
            maxi =  mat[i][c-1]
    desired = (r * c + 1) // 2
    while (mini < maxi):
        mid = mini + (maxi - mini) // 2
        place = [0]
        for i in range(r):
            j = upper_bound(mat[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            mini = mid + 1
        else:
            maxi = mid
    print ("Median is", mini)
    return

# Driver code
r, c = 3, 1
mat = [ [1],[2],[3] ]
binaryMedian(mat, r, c)