#Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

def solution(n):
    value=list(range(1,n+n,2))
    output=sum(value)+sum(value[0:n-1])
    return output
