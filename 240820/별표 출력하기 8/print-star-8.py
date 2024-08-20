n = int(input())

status = 1

for _ in range(n):
    if status % 2 !=0:
        print("*") 
    else :
        print("* "*status)


    status += 1