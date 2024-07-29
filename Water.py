x = 0
y = 0
m = 4
n = 3

print("initial state =(0,0)")
print("capacities =(4,3)")
print("goal state =(2,y)")

while(x != 2):
    r = int(input("enter the rule:"))
    if(r == 1):
        x = m
    elif(r == 2):
        y = n
    elif(r == 3):
        x = 0
    elif(r == 4):
        y = 0
    elif(r == 5):
        t = n - y
        y = n
        x = x - t
    elif(r == 6):
        t = m - x
        x = m
        y = y - t
    elif(r == 7):
        y = x + y
        x = 0
    elif(r == 8):
        x = x + y
        y = 0
    else:
        print("invalid rule")
    print(x, y)
