def solution(sequence):
    fails1 = 0
    fails2 = 0
    
    for i in range(len(sequence)-1):
            if sequence[i] >= sequence[i+1]:
                fails1 = fails1 + 1
                
    for i in range(len(sequence)-2):
            if sequence[i] >= sequence[i+2]:
                fails2 = fails2 + 1
    #print(fails1,fails2)
    if (fails1 < 2) and (fails2 < 2):
                
        return True
    else:
        return False 


print(solution([1,3,2,1]))