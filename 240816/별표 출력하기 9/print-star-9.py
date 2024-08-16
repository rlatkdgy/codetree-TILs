n= int(input())

for i in range(n):

    #공백
    for _ in range(n-i-1):
        print(" ", end = " ")
    #별
    for _ in range(2*i+1):
        print("* ", end = "")
    print()