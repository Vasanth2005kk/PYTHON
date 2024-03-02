# count digits 
#no string approach

num=12345
count=0

if num==0:
    count=1
else:
    while num != 0:
        num//=10 # num = num // 10 
        count+=1

print("count digit :",count)    

'''
def fun(num):
    if num//10==0:
        return 1
    else:
        return (1+fun(num//10))
    
output=fun(10)
print(output)
'''
