def mutate_string(string,list_number,latter):
    string_1=string[:list_number]+latter+string[list_number+1:]
    return string_1
if __name__ == '__main__':
    s = input("enter the string:")
    i, c = input("index value and new letter:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
