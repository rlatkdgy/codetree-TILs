n = int(input())



for i in range(n):
    
    for _ in range(n-i-1):
        print(end= " ")
    for _ in range(i-n):
        print()
    print()