supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
print(supplies.index('pens'))
supplies.insert(1, 'books')
supplies.append('watchs')
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
spam.reverse()
print(spam)