n = int(input())


#별 갯수 (2 * n) - (2 * i) - 1



for a in range(0, n+1):
    
    for b in range((2*n) -(2*a) -1 ):
        print("* ", end = "")
    print(" ")
    print(end ='  '*(a+1))