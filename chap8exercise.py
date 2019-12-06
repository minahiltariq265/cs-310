fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word= line.rstrip().split()    
    for element in word:           
        if element in lst:         
            continue               
        else :                     
            lst.append(element)    
lst.sort()                       
print(lst)

fn=input('enter:')
fhand = open(fn)
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'from':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)   
                      
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))

