n = int(input())  


num = 1


for i in range(n):

    print("  " * i, end="") 

  
    for j in range(n - i):
        print(num, end=" ")
        num += 1
        if num > 9: 
            num = 1
    print()