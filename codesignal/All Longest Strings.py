def solution(inputArray):
    len_store=[]
    output=[]

    for i in inputArray:
        len_store.append(len(i))

    s=max(len_store)

    for j in inputArray:
        if s == len(j):
            output.append(j)
    return output
inputArray=["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]
solution(inputArray)