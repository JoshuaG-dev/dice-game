import random

print("\nWelcome to the dice roll game! Type the word 'Go' when you're ready to roll!")

user_input = ''
while user_input.lower() != 'go':
    user_input = input("\nType here: ")
    if user_input.lower() != 'go':
        print("\nOops! Please type 'Go' when you're ready to roll!")

number = random.randint(1, 6)
print(f"\nYou rolled a {number}!\n")


while True:
    user_input = input('\nWould you like to roll again? If so, type "again" here: ')
    if user_input.lower() == 'again':
        number = random.randint(1, 6)
        print(f"\nYou rolled a {number}!")
    else:
        break