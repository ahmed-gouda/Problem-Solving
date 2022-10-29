for i in range(int(input())):
    x=list(map(int,input().split()))
    a=x[0]
    b=x[1]
    c=x[2]
    sums=[a+b,a+c,b+c]
    if c  == a+b or a==b+c or b==a+c:
        print("YES")
    else:
        print("NO")