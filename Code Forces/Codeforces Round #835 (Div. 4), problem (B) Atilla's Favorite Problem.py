alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    l=int(input())
    s=input()
    x=list(s)
    x.sort()
    ind=alpha.index(x[-1])
    print(ind+1)