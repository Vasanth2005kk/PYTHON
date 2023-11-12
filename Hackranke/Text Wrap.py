import textwrap
def wrap(string, max_width):
    # create a list for the wrapped text and create a empty string
    wrap_lst = textwrap.wrap(string, max_width)
    letters = ""
   # print(wrap_lst)

    # loop through wrap_lst and unpack and add to letters string
    for sub_lst in wrap_lst:
        letters += sub_lst + " "
    letters_1=" "
    # split the letters string by newline so it has its format
    letters = letters.split(" ")
    letters_1= "\n".join(letters)
    return letters_1
if __name__ == '__main__':
    string, max_width = input("enter:"), int(input("enter the number:"))
    result = wrap(string, max_width)
    print(result)