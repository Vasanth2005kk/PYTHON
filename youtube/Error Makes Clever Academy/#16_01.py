
'''create a class called laptop and create a following variable and functio.
variable=price,processor ,ram
create object HP,DELL,LENOVO
'''
class laptop:
    def hp(self,price,processor,ram):
        print("price:",price)
        print("processor:",processor)
        print("ram:",ram)

    def dell(self,price,processor,ram):
        print("price:",price)
        print("processor:",processor)
        print("ram:",ram)

    def lenova(self,price,processor,ram):
        print("price:",price)
        print("processor:",processor)
        print("ram:",ram)
print("press the name or option:")
print(" 1.hp \n 2.dell \n 3.lenova")
choice=input("enter:")
if choice=="1" or choice=="hp":
    # hp
    hp = laptop()
    hp.hp(50000, "core i3", "4gb")
elif choice=="2" or choice=="dell":
    # dell
    dell = laptop()
    dell.dell(75000, "intral 3i r11", "6gb")
elif choice=="3" or choice=="lenova":
    # lenova
    lenova = laptop()
    lenova.lenova(90000, "AMD vi3", "8gb")
