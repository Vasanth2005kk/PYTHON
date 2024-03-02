import time

letters="abcdefghijklmnopqrstuvwxyz"

for i in letters:
    single_letter=input("enter letter:").lower()
    if i != single_letter:
        print("game over !")
        break
else:
    end=time.time()
    print(f"commpleted {round(end,2)} second")
