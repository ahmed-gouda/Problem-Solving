#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t,a[4],c=0;
    cin>>t;
    while (t--)
    {   c=0;
        for(int i=0;i<4;i++)
        {
            cin>>a[i];

        }


            for(int i=0;i<4;i++)
        {
            if(a[0]<a[i])
                c++;


        }
        cout<<c<<endl;
        continue;

        }







}
