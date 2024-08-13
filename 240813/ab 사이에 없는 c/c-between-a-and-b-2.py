a, b, c = map(int, input().split())
state = False


for i in range(a, b+1):
    if i % c == 0:
        state = True

if state == True:
    print("NO")
else :
    print("YES")