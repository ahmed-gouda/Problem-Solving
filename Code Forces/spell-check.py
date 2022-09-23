#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t=int(input())
while (t!=0):
    n=int(input())
    s=input()
    ct=ci=cm=cu=cr=int(0)    
    for i in range (0,n):
        if(s[i]=='T'):
            ct+=1
        elif(s[i]=='i'):
            ci+=1
        elif(s[i]=='m'):
            cm+=1
        elif(s[i]=='u'):
            cu+=1
        elif(s[i]=='r'):
            cr+=1
    if(ct==1 and ci==1 and cm ==1 and cu==1 and cr==1 and n==5):
        print("YES")
    else :
        print("NO")
    t-=1


# In[ ]:





# In[ ]:





# In[ ]:




