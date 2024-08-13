n = int(input())
state = False

for i in range(2, n):
    if n % i ==0:
        state = True
        break
if state == True:
    print("C")
else : 
    print("N")