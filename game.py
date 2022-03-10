import random
javab = random.randint(1, 99)

print('Hi. weloome to number game! I have a number. you must say a guess in range 1,99 .')
name = input('What is your name?: ')
hads = int(input('What is your guess?: '))

while hads != javab:
    if hads > javab:
        print('mine is smaller!')
    else:
        print('mine is bigger!')
    hads = int(input('What is your guess?: '))
    
print('ohhhhhh', name, 'you did it!!!!!!')