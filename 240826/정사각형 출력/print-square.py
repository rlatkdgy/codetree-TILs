n =int(input())

num = 0


for i in range(1, n*n +1):
    print(i, end=" ")
    num += 1
    if num % n==0:
        print()