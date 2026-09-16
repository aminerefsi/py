while True:
    print('who are you:')
    name = input('>')
    if name != 'Amine':
        continue
    print('hello ' + name + '! what is your password? (is it a fish ?)')

    password = input('>')
    if password == 'swordfish':
        break
    print('Try again')

print(f"Hello, {name}! Welcome to the program.")

