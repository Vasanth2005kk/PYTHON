arr=[-1, 150, 190, 170, -1, -1, 160, 180]


#print(list(enumerate(arr)))

def solution(a):

    l = sorted([i for i in a if i > 0])
    #print(l)
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l
    
print(solution(arr))