import random

while True:
    choice = input('Wanna play die game? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for playing the die game!!')
        break
    else:
        print('Invalid choice')