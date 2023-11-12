def average(array):
    n=set(array)
    count = 0
    for i in n:
        count += i
    div = count / len(n)
    return div
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)