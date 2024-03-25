def solution(n):
    if len(str(n)) == 2:
        count=0
        for i in str(n):
            count+=int(i)
        return count
    
print(solution(29))  # 2+9 = 11