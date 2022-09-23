#!/usr/bin/env python
# coding: utf-8

# In[46]:


s=input()
t=input()
l1=len(s)
l2=len(t)
v=0


for i in range (0,l1):
    
        l2-=1
        if(s[i]==t[l2]):
            v+=1
    
    

        
if (v==l1 and len(s)==len(t)):
    print("YES")
else :
        print("NO")




# In[45]:


for i in range (0,l1):
            l2-=1
            if(s[i]==t[l2]):
                v+=1


# In[ ]:


if(l1!=l2):
      print("NO")
      break
  else:  


# In[ ]:




