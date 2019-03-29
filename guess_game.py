from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guessed_number = randint(1, 100)
previous_answer = None
answer_count = 0

while True:
    answer = int(input("Enter number: "))
    distanse = abs(answer - guessed_number)

    if answer < 1 or answer > 100:
        print('Out of bound'.upper())
        continue

    if answer == guessed_number:
        print(f'Congratultions! {answer} is correct!')
        print(f'You answered {answer_count} times')
        break

    if answer_count == 0:
        if distanse <= 10:
            print('Warm!'.upper())
        else:
            print('Cold!'.upper())
    else:
        if distanse < previous_answer:
            print('Warmer!'.upper())
        else:
            print('Colder!'.upper())
    previous_answer = distanse
    answer_count += 1
    continue                