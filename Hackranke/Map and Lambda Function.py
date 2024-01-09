cube = lambda x: pow(x, 3)

def fibonacci(n):
     if n == 1:
        return [0]
     x, y, lst = 0, 1, []
     for _ in range(n):
        lst.append(x)
        # x, y = y, x + y
        nth=x+y
        x=y
        y=nth
     return lst
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#2
'''
def fibonacci(number):
     stored_list=[]
     num_1=0
     num_2=1
     count=0
     output=[]

     for _ in range(0,number):
          while count < number:
               stored_list.append(num_1)
               nth = num_1 + num_2
          # update values
               num_1 = num_2
               num_2 = nth
               count += 1
     #print(stored_list)

     for i in stored_list:
          output.append(i*i*i)
'''
#fibonacci program
'''
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
'''