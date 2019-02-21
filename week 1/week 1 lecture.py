# simple hello world
x= 'Hello World'
i=0
for i in range(len(x)):
    print(x[i])
    i=i+1

print('\n\n\n\n')

# This program display a triangle pattern
BASE_SIZE = 6
for r in range(BASE_SIZE):
    for C in range(r+1):
        print('*', end='')
    print()



print('\n\n\n\n')


# break and coutinue
list1= [2,4,-3,4]
for num in list1:
    if (num<0):
        break
    print(num)
print('\n\n\n')
for num in list1:
    if (num<0):
        print('*')
        continue
    print(num)
print('\n\n\n')

# nested list for Matrix

matrix = [[2,5,-11],[2,2,0],[4,-1,-45]]

# |2  5 -11|
# |2  2  0 |
# |4 -1 -45|


print('\n\n\n')
