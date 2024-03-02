import secrets #or random

numbers=[i for i in range(1,11)]
num=secrets.choice(numbers)
#print(num)
input_number=int(input("Enter the number 1-10:"))

if num == input_number:
    print("\n<---------------------->\nyou're win\n<---------------------->")
else:
    print(f"\nit's not corect,pleass try again \n\n<---------------------->\nanswer:{num}\n<---------------------->")