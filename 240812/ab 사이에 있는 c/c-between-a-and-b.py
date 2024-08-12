a, b, c = map(int,input().split())
cnt1 = 0
cnt2 = 0

while a <= b:
    if a % c ==0:
        cnt1 += 1
    a += 1
if cnt1 == 0:
    print("NO")
else:
    print("YES")