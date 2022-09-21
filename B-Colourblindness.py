t=int(input())
while(t!=0):
    idd=int(0)
    n=int(input())
    s1=input()
    s2=input()
    for i in range(0,n):
        if(s1[i]=='B' and s2[i]=='R'):
            idd=1
            break
        elif(s1[i]=='G' and s2[i]=='R'):
            idd=1
            break
        elif(s1[i]=='R' and s2[i]=='G'):
            idd=1
            break
        elif(s1[i]=='R' and s2[i]=='B'):
            idd=1
            break
            
    if(idd==1):
        print("NO")
    else:
        print("Yes")
    t-=1
        