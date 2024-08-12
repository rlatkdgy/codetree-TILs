a, b, c = map(int,input().split())


while a <= b:
    if a % c ==0:
        print("YES")
    else :
        print("NO")
    a += 1