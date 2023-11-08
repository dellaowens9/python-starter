import random 


random_number = random.randint(1, 100)

if random_number < 10:
    print(f"{random_number}: You lose.")
elif random_number > 10 and random_number <= 50:
    print(f"{random_number}: Try again.")
elif random_number > 50:
    print(f"{random_number}: You win!")