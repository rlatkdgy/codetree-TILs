n = int(input())

cnt = 'A'


for i in range(1, n+1):

    for _ in range(i):
        if cnt == 'Z':
            cnt = 'A'
        print(cnt, end="")
        cnt = chr(ord(cnt)+1)
        
    print()