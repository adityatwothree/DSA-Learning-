T = int(input())

for _ in range(T) :
    arr=[]
    N= int(input())
    for each_food in range(N) :
        x,y,z = (int (A) for A in input().split(' '))
        profit = (y //(x+1))*z 
        arr.append(profit)
    print(max(arr))