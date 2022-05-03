// Readable version

#include <stdio.h>
void f(int i){char s[5]="NSWE\n";printf("%c",s[i]);}
int main(){
    int q,w,e,r;
    scanf("%d%d%d%d",&q,&w,&e,&r);
    while(1)
    {
        if(r>w){f(0);r--;}
        if(r<w){f(1);r++;}
        if(e>q){f(2);e--;}
        if(e<q){f(3);e++;}
        f(4);
    }
}

// Code golf

#include <stdio.h>
void f(int i){char s[5]="NSWE\n";printf("%c",s[i]);}
int main(){int q,w,e,r;scanf("%d%d%d%d",&q,&w,&e,&r);while(1){if(r>w){f(0);r--;}if(r<w){f(1);r++;}if(e>q){f(2);e--;}if(e<q){f(3);e++;}f(4);}}