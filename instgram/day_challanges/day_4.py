#armstrong number or not 

def armstrong(num):
    total_len=len(str(num))

    count=0

    for i in str(num):
        count+=pow(int(i),total_len)

    if count==num:
        print("armstrong number :",num)
    else:
        print("not armstrong number :",num)

number=153 
armstrong(number)

number=123 
armstrong(number)