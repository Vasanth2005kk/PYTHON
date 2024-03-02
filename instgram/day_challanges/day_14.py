# filter element from array

array=[-5,2,-2,-9]

for i in array[:]: #[:] this copy short mathod or array.copy
    if i < 0:
        array.remove(i)

print("only for passitive number :",array)