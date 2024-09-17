N = int(input())

cnt = 'A'
n = N

for j in range(N):
    print("  "*j, end="")

    for i in range(n):
        
        
        print(cnt, end=" ")
        cnt = chr(ord(cnt)+1)
        if cnt > 'Z':
            cnt = 'A'
    n -=1
    print()