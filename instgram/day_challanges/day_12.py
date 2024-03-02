#count element in the array odd and even

array=[12,5,8,23,17,9]

odd=0
even=0

for i in array:
    if i%2 == 0:
        even+=1
    else:
        odd+=1

print("odd number count :",odd)
print("Even number count :",even)



