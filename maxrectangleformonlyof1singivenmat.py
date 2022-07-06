# Expected Time Complexity : O(n*m) , Expected Auixiliary Space : O(m)
'''
Input:
0 1 1
1 1 1
0 1 1      
Output:
6
Explanation : 
The largest rectangle with only 1's is from 
(0, 1) to (2, 2) which is
1 1
1 1
1 1
'''


def rectangle(mat):
    width=len(mat[0])
    height=len(mat)
    max_mat=[[None for v in row]for row in mat]
    def get_max(i,j):
        if i>=width:
            return 0,0
        elif j>=height:
            return 0,0
        elif max_mat[j][i] is not None:
            return max_mat[j][i]
        elif mat[j][i]==0:
            max_mat[j][i]=0,0
            return max_mat[j][i]

        max_down=get_max(i,j+1)
        max_right=get_max(i+1,j)
        max_mat[j][i]=(max_right[0]+1,max_down[1]+1)
        return max_mat[j][i]

    max_rect=0
    for i in range(width):
        for j in range(height):
            rect=get_max(i,j)
            curr_max=rect[1]
            for k in range(1,rect[0]):
                curr_max=min(curr_max,get_max(i+k,j)[1])

            max_rect=max(max_rect,curr_max*rect[0])
    return max_rect

mat=[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
print(f'{mat}')

ans=rectangle(mat)
print(ans)
