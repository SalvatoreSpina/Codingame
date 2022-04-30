// Normal version

#include<iostream>
#define a std::cout<<
int main()
{
    int q,w,e,r;
    std::cin>>q>>w>>e>>r;
    for(;;)
    {
        if(r>w)a"N",r--;
        if(r<w)a"S",r++;
        if(e>q)a"W",e--;
        if(e<q)a"E",e++;
        a"\n";
    }
}

// Code golf version

#include<iostream>
#define a std::cout<<
int main(){int q,w,e,r;std::cin>>q>>w>>e>>r;for(;;){if(r>w)a"N",r--;if(r<w)a"S",r++;if(e>q)a"W",e--;if(e<q)a"E",e++;a"\n";}}