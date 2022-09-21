#include<iostream>
#include<string>
using namespace std;
int main()
{
int t=0,n=0,ct=0,ci=0,cm=0,cu=0,cr=0;
string s;
cin>>t;
while(t--)
{   ct=ci=cm=cu=cr=0;
    cin>>n;
    cin>>s;
    for(int i=0 ;i<n;i++)
    {

        if(s[i]=='T')
            ct++;
        else if(s[i]=='i')
            ci++;
        else if(s[i]=='m')
            cm++;
        else if(s[i]=='u')
            cu++;
        else if(s[i]=='r')
            cr++;



    }

    if(n==5&ct==1&&ci==1&&cm==1&&cu==1&&cr==1)
        cout<<"YES"<<endl;
    else cout<<"NO"<<endl;




}



return 0;
}
