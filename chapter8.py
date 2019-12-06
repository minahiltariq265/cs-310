cheeses = ['Cheddar', 'Edam', 'Gouda'] 
numbers = [17, 123]
empty = [] 
print(cheeses, numbers, empty) 

numbers = [17, 123] 
numbers[1] = 5 
print(numbers)  

cheeses = ['Cheddar', 'Edam', 'Gouda'] 
'Edam' in cheeses
'Brie' in cheeses 

for cheese in cheeses: 
    print(cheese) 

for i in range(len(numbers)): 
    numbers[i] = numbers[i] * 2
print(numbers[i])

for x in empty: 
    print('This never happens.')

a = [1, 2, 3] 
b = [4, 5, 6]
c = a + b
print(c) 

t = ['a', 'b', 'c', 'd', 'e', 'f'] 
t[1:3]
t[:4]
t[3:] 
t[:] 

t = ['a', 'b', 'c', 'd', 'e', 'f'] 
t[1:3] = ['x', 'y'] 
print(t)

t1 = ['a', 'b', 'c'] 
t2 = ['d', 'e'] 
t1.extend(t2)
print(t1)  

t4=['d','c','e','a','b']
t4.sort()
print(t4)

t5=['a','b','c']
x=t5.pop(1)
print(t5)
print(x)  
del t5[1]
print(t5)

t6=['a', 'b', 'c'] 
t6.remove('b')
print(t6)

total = 0 
count = 0 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': 
        break 
    value = float(inp) 
    total = total + value 
    count = count + 1
average = total / count 
print('Average:', average)

numlist = list() 
while (True): 
    inp = input('Enter a number: ') 
    if inp == 'done': 
        break 
    numlist.append(value)

    average = sum(numlist) / len(numlist) 
    print('Average:', average)
    quit()

s = 'spam' 
t = list(s)
print(t) 

g = 'pining for the fjords'
l = g.split()
print(l)
print(l[2]) 

cut = 'spam-spam-spam'
delimiter = '-' 
cut.split(delimiter) 

