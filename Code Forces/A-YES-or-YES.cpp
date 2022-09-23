#include <iostream>
#include<string>
using namespace std;

int main()
{
    int n;
    cin>>n;
    string checkword[n] ;
    for(int i=0;i<n;i++)
    {
        cin >>checkword[i];

    }
    for(int i=0;i<n;i++)
    {
        if(checkword[i]=="YES"||checkword[i]=="YEs"||checkword[i]=="Yes" ||checkword[i]=="yes"
           ||checkword[i]=="yeS"||checkword[i]=="YeS"||checkword[i]=="yEs" ||checkword[i]=="yES" )
            cout<<"YES"<<endl;
            else cout <<"NO"<<endl;

    }

    return 0;
}
