n = int(input())


for i in range(n):
    #앞에 공백 먼저
    for _ in range(i):
        print(end ="  ")


    #그다음에 패턴

    for _ in range((2 * n) - (2 * i) - 1):
        print("* ", end="")
    print()

for b in range(n-1):   
    for _ in range(n - b - 2):
        print(end="  ")
    for _ in range(3 + (2 * b)):
        print("* ", end="")    
    print()