# Normal version

n,a=int(input()),[int(i)for i in input().split()]
m=(0,999)[n>0]
for i in a:m=(m,i)[abs(m)>abs(i)or(abs(m)==abs(i)and i>m)]
print(m)

# Code golf

s=abs
z=int
w=input
n,a=z(w()),[z(i)for i in w().split()]
m=(0,999)[n>0]
for i in a:m=(m,i)[s(m)>s(i)or(s(m)==s(i)and i>m)]
w(m)