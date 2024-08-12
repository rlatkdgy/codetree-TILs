a = 1
cnt = 0
N = int(input())

while True:
    a *= 2
    cnt += 1
    if N==a:
        break
   

print(cnt)