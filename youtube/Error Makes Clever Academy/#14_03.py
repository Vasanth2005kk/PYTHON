'''get a intger number form user and pass it to the function called
findpassorfail(). let the function print whether the number is pass or
fail'''
def findpassorfail(number):
    if number>=35:
        print("pass")
    else:
        print("fail")

mark=int(input("enter the mark:"))
findpassorfail(mark)
