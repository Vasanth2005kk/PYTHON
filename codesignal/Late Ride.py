def solution(n):
    #print(str(n // 60 * 100 + n % 60))
    return sum(map(int, str(n // 60 * 100 + n % 60)))

n=23
print(solution(n))

'''
n=23

def solution(n):
    count=0
    if len(str(n))==2:
        for i in str(n):
            count+=int(i)
        return count
    else:
        mint=n//60
        sec=n-(mint*60)

        for i,j in zip(str(mint),str(sec)):
            count+=int(i)+int(j)

        return count

print(solution(n))'''