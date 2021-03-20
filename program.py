import random


random_number = random.randint(1, 10)
answer = int(input("Guess number between 1 and 10: "))
while True:
    if random_number == answer:
        print("You guessed number {}".format(answer))
        break
    elif random_number > answer:
        print("To low")
        answer = int(input("Try again, enter number: "))
        continue
    elif random_number < answer:
        print("To high")
        answer = int(input("Try again, enter number: "))
        continue
