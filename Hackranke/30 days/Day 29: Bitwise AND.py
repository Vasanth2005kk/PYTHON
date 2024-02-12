def bitwiseAnd(N, K):
    bit_max = 0
    for a in range(N):
        for b in range(a + 1, N + 1):
            if bit_max < a & b < K:
                bit_max = a & b
    return bit_max

T=int(input())
for i in range(T):
    variable=list(map(int,input().split(" ")))
    print(bitwiseAnd(variable[0],variable[1]))