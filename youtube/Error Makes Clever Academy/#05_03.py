'''get input fora number and check whwther it is divisible by both 3 and
5 or not. if yes then print , the number is divisible by 3 and 5 else print
the number is not divisble by 3 and 5'''
number=int(input("enter the number :"))
if number%3==0 and number%5==0:
    print("the",number,"is divisible by 3 and 5")
else:
    print("the",number,"is not divisible by 3 and 5")
