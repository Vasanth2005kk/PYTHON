N = int(input())

MARK_STORE = []
HEADERS = input().split(" ")
MARK_INDEX = HEADERS.index("MARKS")

for i in range(N):
    datas = input().split(" ")
    MARK_STORE.append(datas)

total = 0
for j in range(len(MARK_STORE)):
    total += int(MARK_STORE[j][MARK_INDEX])

print("{:.2f}".format(total / N))



# from collections import namedtuple
# n = int(input())
# # print(n)
# columns = input()
# print(columns)
# Students = namedtuple("Student", columns)
# print(Students)
# st = Students
# sm = 0
# for _ in range(n):
#     s = input().split()
#     print(*s)
#     st = Students(*s)
#     sm += int(st.MARKS)
# print(sm/n)