d=[]
strength_of_player,number_of_dragons=map(int,input().split())
for i in range(number_of_dragons):  
    strength_of_dragon,bonus=map(int,input().split())
    d.append([strength_of_dragon,bonus])
d.sort()
for i  in range(len(d)):
    if strength_of_player<=d[i][0]:
        print('NO')
        break
    elif i==len(d)-1:
        print("YES")
    elif strength_of_player>d[i][0]:
        strength_of_player+=d[i][1]