# n = int(input())
# tree = [list(map(int,(input()))) for _ in range(n)]


n = 8
tree = [[1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0], [0,0,0,1,1,1,0,0], [0,0,0,1,1,1,0,0], [1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0], [1,1,1,1,0,0,1,1], [1,1,1,1,0,0,1,1]]

result = []

def quad_tree(x,y,n):
    color = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: 
                result.append("(")
                quad_tree(x,y,n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color) 

quad_tree(0,0,n)
# print("".join(map(str,(result))))
print(result)
