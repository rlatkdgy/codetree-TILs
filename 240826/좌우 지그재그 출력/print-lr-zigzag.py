n = int(input())

odd = 1
even =1

for i in range(1, n+1):

    if i % 2 != 0:
        for _ in range(n):
            print(odd,end=" ")
            odd += 1

        print()


    else :

        for c in range(n*i,n*i-n,-1):

            print(c,end=" ")
            odd+=1
        print()

            
            




        pass