num=int(input())
main_input=set(map(int,input().split(" ")))
if num == len(main_input):
    N=int(input())
    for _ in range(N):
        name,number=input().split(" ")
        set_values=set(map(int,input().split(" ")))
        if name == "intersection_update":
            main_input.intersection_update(set_values)
        elif name == "update":
            main_input.update(set_values)
        elif name == "symmetric_difference_update":
            main_input.symmetric_difference_update(set_values)
        elif name == "difference_update":
            main_input.difference_update(set_values)

    print(sum(main_input))

#short method 
'''
main_input={1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,52}

a={2,3,5,6,8,9,1,4,7,11}
main_input.intersection_update(a)
b={55,66}
main_input.update(b)
c={22,7,35,62,58}
main_input.symmetric_difference_update(c)
d={11,22,35,55,58,62,66}
main_input.difference_update(d)

print(sum(main_input))
'''