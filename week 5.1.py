spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[3])
spam[1] = 'dog'
print(spam[0:4])
spam[-1] = '123'
print(spam[3])
print(spam[-1])
spam = spam + ['x', 'y', 'z']
print(spam)
del spam[4]
print(spam)