my_pets = ['ciaco', 'silver', 'moon']
print('enter a pet name: ')
name = input()
if name not in my_pets:
    print('i do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
