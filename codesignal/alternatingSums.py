def solution(arr):
    odd_index=[]
    even_index=[]

    for i in range(len(arr)):
        if i%2==1:
            even_index.append(arr[i])
        else:
            odd_index.append(arr[i])

    return [sum(odd_index),sum(even_index)]

        
