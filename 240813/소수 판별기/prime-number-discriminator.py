n = int(input())
state = True


for i in range(2, n):
    if n % i ==0:
        state = False
if state == False:
    print("C")
else :
    print("P")