I,S,N=input,str.split,int
*_,f,p,t,a,e=S(I())
t={f:p,**dict([S(I())for _ in[1]*N(e)])}
while 1:f,p,d = S(I());print(('BLOCK','WAIT')['-'in p or(N(p)-N(t[f]))*d.find('I')<1])