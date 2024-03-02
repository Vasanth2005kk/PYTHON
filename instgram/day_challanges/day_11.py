#search element in the array

array=[12,5,8,23,17,9]
target=23

if target in array:
    print("Element found index :",array.index(target))
else:
    print("Element not found")