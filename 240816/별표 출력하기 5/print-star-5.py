n = int(input())

for _ in range(n):
    for _ in range(n):
        print("*"*n, end=" ")
    n -= 1
    print()