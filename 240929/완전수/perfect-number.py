start, end = map(int, input().split())



cnt = 0
a = 0 
while start <= end:

    for i in range(1, start):
        if start % i ==0:
            a += i
    if a == start:
        cnt += 1
    a=0


    start += 1
print(cnt)