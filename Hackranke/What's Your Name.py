def print_full_name(frist_name,last_name):
    n=last_name.__add__("!")
    print("Hello",frist_name,n,"You just delved into python.")
    return print_full_name
if __name__ == '__main__':
    first_name = input("first name:")
    last_name = input("last name:")
    print_full_name(first_name, last_name)
