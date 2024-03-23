n=1230

def solution(n):
    number_to_string=list(str(n))

    indexing=len(number_to_string)//2

    #print(number_to_string)
    #print(indexing)

    if len(number_to_string)%2==0:
        if sum([int(i) for i in number_to_string[0:indexing]]) == sum([int(j) for j in number_to_string[indexing:]]):
            return True
        else:
            return False
    else:
        return False

print(solution(n)) 