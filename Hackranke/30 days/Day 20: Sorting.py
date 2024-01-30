if __name__ == '__main__':
    n = int(input().strip())
    
    a = list(map(int, input().rstrip().split()))
    swaps = 0
    for _ in range(len(a)):
        for i in range (len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1 
    print (f"Array is sorted in {str(swaps)} swaps.")
    print (f"First Element: {a[0]}")
    print (f"Last Element: {a[len(a)-1]}")