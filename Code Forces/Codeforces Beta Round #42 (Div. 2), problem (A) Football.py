x=[]
for i in range(int(input())):
    a=input()
    x.append(a)
s=set(x)
l=list(s)
if len(x)==1:
    print(x[0])
elif x.count(l[0])>x.count(l[1]):
    print(l[0])
else:
    print(l[0])