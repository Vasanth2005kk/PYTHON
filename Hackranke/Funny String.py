def funny_string(string):
    normal_string=[]
    reversed_string=[]

    output_1=[]
    #output_2=[]

    for i in string:
        normal_string.append(ord(i))

    for j in string[::-1]:
        reversed_string.append(ord(j))


    for i in range(len(normal_string)-1):
        noraml_values=normal_string[i]-normal_string[i+1]
        #output_1.append(abs(noraml_values))

        reversed_values=reversed_string[i]-reversed_string[i+1]
        #output_2.append(abs(reversed_values))

        if abs(noraml_values) == abs(reversed_values) :
            output_1.append(True)
        else:
            output_1.append(False)

    if all(output_1):
        print("Funny")
    else:
        print("Not Funny")

num=int(input())
for i in range(num):
    string=input()
    funny_string(string=string)


