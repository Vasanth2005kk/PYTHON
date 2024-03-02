#search element in the array

array=[12,5,8,23,17,9]
target=23

if target in array:
    print("Element found index :",array.index(target))
else:
    print("Element not found")

'''
#list_input=map(int,input().strip("[]").split(","))

a=[1,2,3,4,5,6,7]
target=7

count=0
if target in a:
    for i in a:
        if i == target:
            break
        else:
            count+=1
    print("element found index:",count)
else:
    print("Elenment not found ")
'''