x=0 
y=0
z=0
for i in range(int(input())):
    vector=list(map(int,input().split()))
    x+=vector[0]
    y+=vector[1]
    z+=vector[2]
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')