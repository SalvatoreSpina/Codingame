// Readable version

m=Math.abs
z=readline;
n=z();
(t=z().split(" "))!=''?r=t[0]:r=0
for (j of t){
    l=m(r);
    z=m(j);
    if (l>z || l==z && r<j) r=j
}
print(r)

// Code Golf

m=Math.abs;z=readline;n=z();(t=z().split(" "))!=''?r=t[0]:r=0
for(j of t){l=m(r);z=m(j);if(l>z||l==z&&r<j)r=j}print(r)