// Readable version

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int t,r=0;
    for(int i=0;i<n;++i)
    {
        cin>>t;
        if (i==0||(abs(t)<abs(r))||(abs(t)==abs(r)&&t>r))
            r=t;
    }
    cout<<r<<endl;
}

// Code Golf

#include <iostream>
using namespace std;main(){int n;cin>>n;int t,r=0;for(int i=0;i<n;++i){cin>>t;if(i==0||(abs(t)<abs(r))||(abs(t)==abs(r)&&t>r))r=t;}cout<<r<<endl;}