#include <iostream>

using namespace std;

int main()
{
    int n; //number of games played
    string g; //first letter of the winner of every game
    int a=0 ,d=0;
    cin>>n>>g;
    for (int i =0 ;i<n;i++)
    {
       if (g[i]=='A') a++;
       else if (g[i]=='D') d++;
    }
    if (a==d)cout<<"Friendship";
    else if (a>d)cout<<"Anton";
    else cout<<"Danik";
        return 0;
}