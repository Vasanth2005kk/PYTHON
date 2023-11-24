def merge_the_tools(string, k):
    # your code goes here
    def functaon(x):
        return item.index(x)
    from textwrap import wrap
    clips = wrap(string,k)
#print(clips)
    for item in clips:
        temp_set = list(set(item))
        temp_set.sort()
        #print(temp_set)
        temp_set.sort(key=functaon)
        print("".join(temp_set))

if __name__ == '__main__':
    string, k = input("enter the string:"), int(input("enetr the rows:"))
    merge_the_tools(string, k)
#sort example
'''# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
'''