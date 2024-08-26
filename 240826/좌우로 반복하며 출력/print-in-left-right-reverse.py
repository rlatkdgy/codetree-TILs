n = int(input())




for i in range(1, n+1):
    # 홀수항 ex. 1,3,5,7....
    if i % 2 != 0:
        for a in range(1, n+1):
            print(a,end="")
        print()
    else:
        for a in range(n,0,-1):
            print(a,end="")
        print()