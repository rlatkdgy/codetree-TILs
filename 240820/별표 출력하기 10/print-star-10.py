n= int(input())

c = n
b= 1



for i in range(1, 2*n+1):
    if i % 2 !=0:
        print("* "*b)
        b+=1
    else:
        print("* "*c)
        c -=1