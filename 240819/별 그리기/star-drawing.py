n = int(input())




for i in range(n):
    for _ in range(n-(i+1)):
        print(end= " ")

    for _ in range(2*i + 1):
        print("*", end= "")
    print()
for a in range(n):
    for _ in range(a + 1):
        print(end = " ")
    for _ in range((2*n) - (2*a)-3):
        print("*", end="")
    print()