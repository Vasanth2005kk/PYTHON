
def grade(mark):
    if not(mark <=35):
        for i in range(0,6):
            ans=mark+i
            if ans%5 == 0:
                if ans-mark < 3:
                    return ans
                else:
                    return mark
    else:
        return mark

for i in range(int(input())):        
    output=grade(int(input()))
    print(output)