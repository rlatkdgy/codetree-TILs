n = int(input())



for i in range(1,n+1):
    for a in range(1, n+1):
        print(f"{i} * {a} = {i * a}", end="")
        if a < 3:
            print(",", end =" ")
    print()