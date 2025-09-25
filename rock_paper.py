import random 

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('p','s','r')
user_choice = input('rock, paper and scissors? (r/p/s): ').lower()
if user_choice not in choices:
    print('Invalid input.')
computer_choice = random.choice(choices)
print(f'You chose {emojis[user_choice]}')
print(f'Computer chose {emojis[computer_choice]}')