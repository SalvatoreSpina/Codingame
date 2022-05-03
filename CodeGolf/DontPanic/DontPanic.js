z=readline;
[,,,t,y,,,u]=z().split(' ');e=[];[b,w,o,l]=["BLOCK","WAIT","RIGHT","LEFT"]
for(i=0;i<u; i++)a=z().split(' '),e[~~a[0]]=~~a[1]
while(1)[f,p,d]=z().split(' '),f=~~f,p=~~p,f<0||f==t?(g=y-p>0?o:l,r=g!=d?b:w):(q=e[f],h=q-p>0?o:l,r=q-p==0?w:h!=d?b:w),print(r)