// Readable version

#include <iostream>
using namespace std;
int main()
{
    int n,w,r,x,p,t,a,e,f,o,c,l,v[15],u=0,i=0,s;
    cin>>n>>w>>r>>x>>p>>t>>a>>e;
    for(;i<e;i++)
    {
        cin>>f>>o;cin;
        v[f]=o;
    }
    while(1)
    {
        string d,m="WAIT";
        cin>>c>>l>>d;; 
        if(c==u){s=(x==c)?p:v[c];
        if((d=="RIGHT"&&l>s)||(d=="LEFT"&&l<s))m="BLOCK";u++;}
        cout<<m<<endl;
    }
}

// Code Golf

#include <iostream>
using namespace std;main(){int n,w,r,x,p,t,a,e,f,o,c,l,v[15],u=0,i=0,s;cin>>n>>w>>r>>x>>p>>t>>a>>e;for(;i<e;i++){cin>>f>>o;cin;v[f]=o;}while(1){string d,m="WAIT";cin>>c>>l>>d;;if(c==u){s=(x==c)?p:v[c];if((d=="RIGHT"&&l>s)||(d=="LEFT"&&l<s))m="BLOCK";u++;}cout<<m<<endl;}}