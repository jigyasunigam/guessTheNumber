import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    lives = 7
    while guess != random_number and lives>0:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        lives-=1
        print('you have',lives,'lives left')
        if(lives==0):
            print("game over")
            break
        if(random_number==guess):
            print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
guess(10)