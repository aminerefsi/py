import sys
while True:
    print('tipe exit to exit the program')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')