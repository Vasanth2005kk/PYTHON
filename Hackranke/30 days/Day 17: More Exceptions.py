import re
import math

class Calculator():
    def power(self,n,p):
        varible=[n,p]
        for i in varible:
            if re.search("^-",str(i)):
                return "n and p should be non-negative"
        else:
            return int(math.pow(n,p))
            


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   