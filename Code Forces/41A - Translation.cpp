#include <iostream>
#include<string.h>
using namespace std;

int main()
{
     string s,t;
     cin>>s>>t;
     int len=s.length(),x=len ,validate=0;

     for (int i=0 ;i<len;i++)
     {
        if (s[i]==t[--x])
            validate++;
     }
     if (validate==len)
        cout <<"YES";
        else cout<<"NO";
}
