def reverse(array,x,i,j):
    while i<j:
        array[x][i],array[x][j]=array[x][j],array[x][i]
        i+=1
        j-=1
def Transpose(array,row):
    for i in range(row):
        for j in range(i+1,row):
            array[i][j],array[j][i]=array[j][i],array[i][j]

def Rotate_Matrix(array,row):
    """
    Approach: first take transpose and reverse tha array row wise
    """
    Transpose(array,row)
    for k in range(row):
        reverse(array,k,0,row-1)

if __name__ == '__main__':
    row=int(input())
    array=[]
    for _ in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    Rotate_Matrix(array,row)
    print(*array)

"""
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).

PS: You aren't allowed to create an additional array
"""
