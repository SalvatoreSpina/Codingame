# Readable version

a,b,c,d=map(int,input().split())
while 1:
    x,y=(c<a)-(a<c),(d<b)-(b<d)
    print((" SN"[y]+" EW"[x]).strip())
    c+=x
    d+=y

# Code golf

a,b,c,d=map(int,input().split())
while 1:x,y=(c<a)-(a<c),(d<b)-(b<d);print((" SN"[y]+" EW"[x]).strip());c+=x;d+=y