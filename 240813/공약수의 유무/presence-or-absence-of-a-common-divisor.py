a, b = map(int, input().split())
state = False


for i  in range(a, b+1):
    if 1920 % i == 0 and 2880 % i ==0:
        state = True
if state == True:
    print("1")
else : 
    print('0')