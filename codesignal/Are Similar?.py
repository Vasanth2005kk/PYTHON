def solution(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)]) <= 2


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

print(solution(a,b))
'''
def solution(a, b):
    output=[]
    output_1=[]
    ans=[]
    for i,j in zip(a,b):
        output.append(str(i))
        output_1.append(str(j))

    for i in output:
        if output.count(i) == output_1.count(i):
            ans.append(True)
        else:
            ans.append(False)
    
    return all(ans)

'''