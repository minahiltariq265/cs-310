#chap5
x=1
y=2
z=3
if((x==y)or(y==z)or(z==2)):
    print('yes')
else:
    print('no')

if(1==2):
    print('Hello')
elif(2==1):
    print('World')
else:
    print('invalid')

angle=input('angle')
if(angle>5):
    angle=angle+5
elif(angle>2):
    angle=angle+10
else:
    angle=angle+15
print(angle)

p=10
q=3
r=-2
if((p+q)<14 and (r<(q-3))):
    print(r)
else:
    print(p)

if('A'=='A') and ('B'=='B') and ('C'=='c'):
    print('equal')
else:
    print('not equal')

if(9<5):
    print('x')
elif(5==6):
    print('#')
else:
    print('@')

a=input('a=')
b=input('b=')
c=input('c=')
if(a>b and a>c):
    m=a
elif(b>c):
    m=b
else:
    m=c
print(m)
 #chap6
 n=4
sum=1
while n<=100:
    sum=sum+(1/n)
    n=n+4
print (sum)

for c in range(65, 91):
    print(chr(c), end = " ");

sum=0
smallest = None
largest= None
for value in[20,21,22,30,40]:
    if smallest is None or value < smallest:
        smallest = value
    if largest is None or value> largest:
        largest=value
    sum=sum+value
print('Smallest:', smallest)
print('Largest: ', largest)
average=sum/5
print(average)



