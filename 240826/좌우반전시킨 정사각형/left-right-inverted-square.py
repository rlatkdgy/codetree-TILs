n = int(input())




for i in range(1, n+1):

    for j in range(i*n,0,-i):
        print(j, end=" ")

    print()