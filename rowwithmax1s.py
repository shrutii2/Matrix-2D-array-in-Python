# The time complexity of the proposed solution is O(M + N) for an M × N matrix 
# and doesn’t require any extra space.

def rowwithmax1(mat):
    if not mat or not len(mat):
        return
    row = -1
    (i, j) = (0, len(mat[0]) - 1)
    while i <= len(mat) - 1 and j >= 0:
        if mat[i][j] == 1:
            j = j - 1
            row = i         
        else:
            i = i + 1
    return row + 1

mat = [
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]

ans = rowwithmax1(mat)
if ans:
    print("The maximum 1's are present in the row", ans)
