def solution(s1, s2):
    s2_copy=s2.copy()
    total=0
    for i in s1:
        if i in s2_copy:
            s2_copy.remove(i)
            total+=1
    print(total)

s1='abca'
s2=list('xyzbac')

solution(s1,s2)