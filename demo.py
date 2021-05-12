A=[] # empty list
size=int(input('Just pass the size of list'))
for i in range(size):
    x=int(input('pass an integer value into the list\n'))
    A.append(x)
print('The list value :',A)
max=A[0]
for i in A:
    if i>max:
        max=i
print('Max value in the list:',max)


