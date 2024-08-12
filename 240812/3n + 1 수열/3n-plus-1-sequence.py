cnt = 0

N = int(input())


while True:
    if N % 2 == 0 :
        N = N / 2
        cnt += 1
    else :
        N = N*3 + 1
        cnt += 1
    if N == 1:
        break

print(cnt)