import random

while True:
    choice = input('Wanna play die game? (y/n): ')
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
   