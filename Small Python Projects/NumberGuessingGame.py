import random

def generate_random_number():
    low_end = int(input('Enter the minimum value of the generated number: '))
    high_end = int(input('Enter the maximum value of the generated number: '))
    return random.randint(low_end, high_end)


random_number = generate_random_number()

max_guesses = int(input('Enter the maxium number of guesses allowed: '))
guess_count = 0
number_guessed = False

while guess_count < max_guesses:
    guess_count += 1
    guess = int(input('Guess the number generated: '))
    if guess == random_number:
        print(f'Congratulations you guess the number in {guess_count} attempts!')
        number_guessed = True
        break
    elif guess < random_number:
        print(f'Incorrect the number is higher than that. You have {max_guesses-guess_count} attempts remaining!')
    elif guess > random_number:
        print(f'Incorrect the number is lower than that. You have {max_guesses-guess_count} attempts remaining!')

if not number_guessed:
    print(f'The number was {random_number}. Better luch next time.')