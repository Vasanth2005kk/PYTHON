
def solution(picture):
    output=[]
    for i in range(len(picture)+2):
        if i==0:
            output.append('*'*(len(picture[0])+2))
        elif i == len(picture)+1:
            output.append('*'*(len(picture[0])+2))
        else:
            output.append('*'+picture[i-1]+'*')

    return output


