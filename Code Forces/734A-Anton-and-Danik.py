n=int(input())
s=(input())
ant=0
dan=0
for x in range (0,n) :
    if (s[x]=='A'):
        ant+=1
    elif (s[x]=='D'):
        dan+=1
if(ant>dan):
    print("Anton")
elif(ant<dan) :
    print("Danik")
elif(ant==dan) :
    print("Friendship")