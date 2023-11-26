a=[3,5,4,6,8,2,23,75,123,67,11,00,1455554432]
b=[]
for item in a:
    if item % 2 ==0:
        b.append(item)
print(b)

b=[i for i in a if i%2==0]
print(b)

t=[1,2,3,4,5,6,7,8,9,0]
s={i for i in t}
print(s)