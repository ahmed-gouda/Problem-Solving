for i in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    s=set(a)
    if n>1:
        if len(s)<len(a):
            print("NO")
        elif a==b:
            print("YES")
        elif a!=b:
            print("YES")
        
    else:
        print("YES")