name = ''
while not name:
    print("Please enter your name:")
    name = input('>')
print("How many ghosts do you have?")
num_ghosts = int(input('>'))
if num_ghosts:
    print(f'be sure to have enough room for all your ghosts!')
print ('done') 