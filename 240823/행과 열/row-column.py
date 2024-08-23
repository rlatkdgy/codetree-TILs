a, b =map(int, input().split())



for i in range(1, a+1):

    for c in range(1, b+1):
        print(f"{i * c}", end =" ")
    print()