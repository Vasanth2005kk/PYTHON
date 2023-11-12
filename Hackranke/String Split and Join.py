def split_and_join(line):
    list_1=[line.split(" ")]
    #print(list_1)
    list_2=""
    for i in list_1:
        list_2 ="-".join(i)
    #print(list_2)
    return list_2


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)