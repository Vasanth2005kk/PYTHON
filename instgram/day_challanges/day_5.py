#find divisors of number

def divisors(num):
    output=[]
    for i in range(1,num+1):
        if num % i ==0:
            output.append(str(i))
    print(",".join(output))


number=12
divisors(number)