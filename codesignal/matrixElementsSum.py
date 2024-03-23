def solution(m):
    r = len(m) #3
    c = len(m[0]) # 4
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

#print(solution())
m=[[0,1,1,2],[0,5,0,0],[2,0,3,3]]
print(len(m[0]))