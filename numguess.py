from random import randint

# Create answer range: 1 to 100(integer)
answer = randint(1,100)
#Print answer(for debugging)
print(answer)

# Get user's name, guess
user_name = input('Hello, there! What is your name? ')
guess = int(input(f'Hi, {user_name}. Guess the number(1-100): '))

# print to check
print(user_name, guess)

# Check add print correct or not
if guess==answer:
    print('Congrats!')
else:
    print(f'Your are wrong! The answer was {answer}.')
