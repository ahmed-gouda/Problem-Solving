#include <iostream>
#include<string>
using namespace std;

int main()
{
   int t=0,id=0;
   cin>>t;
   while(t--)
   { int n=0;
   cin>>n;
   string s1,s2;
   cin>>s1>>s2;
   id=0;
       for (int i=0;i<n;i++)
       {    if((s1[i]=='R'&&s2[i]=='B')||(s1[i]=='B'&&s2[i]=='R')||(s1[i]=='R'&&s2[i]=='G')||(s1[i]=='G'&&s2[i]=='R'))
                id=1;

       }




        if(id==1)
            cout<<"NO"<<endl;
        else
            cout<<"YES"<<endl;




   }
    return 0;
}
