import random 

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('p','s','r')

user_choice = input('rock, paper and scissors? (r/p/s): ').lower()
if user_choice not in choices:
    print('Invalid input.')

computer_choice = random.choice(choices)

print(f'You chose {emojis[user_choice]}')
print(f'Computer chose {emojis[computer_choice]}')

if user_choice == computer_choice:
    print('Tie!!')
elif (
    (user_choice == 'r' and computer_choice == 's')
    (user_choice == 's' and computer_choice == 'p')
    (user_choice == 'p' and computer_choice == 's')):
    print('You win!!')
else:
    print('You lose..😶🤦‍♂️')