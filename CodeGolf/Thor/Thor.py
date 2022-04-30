# Normal version

x,y,X,Y=map(int,input().split())
while 1:m,u=(((["",u],["N",u-1])[u>y]),["S",u+1])[u<y];m,c=((([m,c],[m+"W",c-1])[c>x]),[m+"E",c+1])[c<x];print(m)

# Code golf
a=input()
x,y,X,Y=map(int,a.split())
while 1:if(y>Y)a("N")if(Y>y)a("S")if(X>x)a("W")if()