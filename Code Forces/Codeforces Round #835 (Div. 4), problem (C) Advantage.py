for j in range(int(input())):
    temp=int(input())
    x= list(map(int,input().split()))
    res=[]
    sortedx=x.copy()
    sortedx.sort()
    for i in x:
        if i == sortedx[-1]:
            res.append(i-sortedx[-2])
        else:
            res.append(i-sortedx[-1])
    print(*res,sep=' ')
