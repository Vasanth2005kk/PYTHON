n=10
firstNumber=2
def solution(n, firstNumber):

    numbers=[i for i in range(n)]
    numbers=[numbers[:n//2],numbers[n//2:]]

    #print(numbers)

    if firstNumber in numbers[0]:
        print(numbers[1][firstNumber])

    elif firstNumber in numbers[1]:
        print(numbers[0][numbers[1].index(firstNumber)])

solution(n,firstNumber)