check=[ "YES","YEs","Yes" ,"yes"
           ,"yeS","YeS","yEs" ,"yES" ]
n=int(input())
instr=[]
for i in range (0,n) :
        instr.append(input())
for i in range(0,n):
    if(instr[i] ) in check:
        print("YES")
    else:
        print("NO")