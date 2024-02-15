#Given the string, check if it is a palindrome.

def solution(inputString):
    output=inputString[::-1]
    if output==inputString:
        return True
    else:
        return False