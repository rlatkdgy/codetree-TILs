add = 2
base = 11
num=0

# for i in range(3):

#     for a in range(11, ,2):
#         print(a)

# for i in range(1, n*n + 1):
#     print(base, end = " ")
#     base += 2
#     num += 1
#     if num % n == 0:
#         print()
n = int(input())
plus = 2

for i in range(0, 2 * n, 2):
    for j in range(11, n * plus - 1 + 11, 2):
        print(j + i, end=' ')
    print()