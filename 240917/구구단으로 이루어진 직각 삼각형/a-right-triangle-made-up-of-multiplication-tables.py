n = int(input())


a = n


for i in range(1, n+1):


    for j in range(1, a+1):

        if j < a:

            print(f"{i} * {j} = {i*j}", end = " / ")
        else :
            print(f"{i} * {j} = {i*j}", end = "")

    a -= 1
    print()