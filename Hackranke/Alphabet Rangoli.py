def print_rangoli(n):
    for i in range(n - 1, -1, -1):
        # print(i)
        for j in range(i):
            print(end="--")
        for j in range(n - 1, i, -1):
            print(chr(j + 97), end="-")
        for j in range(i, n):
            if j != n - 1:
                print(chr(j + 97), end="-")
            else:
                print(chr(j + 97), end="")
        for j in range(2 * i):
            print(end="-")
        print()
    for i in range(1, n):
        for j in range(i):
            print(end="--")
        for j in range(n - 1, i, -1):
            print(chr(j + 97), end="-")
        for j in range(i, n):
            if j != n - 1:
                print(chr(j + 97), end="-")
            else:
                print(chr(j + 97), end="")
        for j in range(2 * i):
            print(end="-")
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''import string

letters = list(string.ascii_lowercase)

def print_rangoli(size):
    output_list = []
    width = (size * 2 - 1) * 2 - 1
    size_letters = letters[:size][::-1]

    for i in range(1, len(size_letters) + 1):
        half = "-".join(size_letters[0:i])
        half += half[:-1][::-1]
        output_list.append(half.center(width, "-"))

    output_list.extend(output_list[:-1][::-1])

    for output in output_list:
        print(output)'''