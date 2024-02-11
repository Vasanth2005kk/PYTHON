import re
if __name__ == '__main__':
    N = int(input().strip())
    output=[]
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        email=first_multiple_input[1]

        if re.findall("@gmail.com$",email):
            value=re.split("@",email)
            if re.findall("[a-z,0-9]",value[0]):
                output.append(first_multiple_input[0])
    output.sort()
    for j in output:
        print(j)