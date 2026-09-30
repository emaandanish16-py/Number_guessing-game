import random

secret = random.randint(1, 100)  # computer ka secret number
tries = 0  # koshishon ki ginti

print("Number Guessing Game")
print("Maine 1 se 100 ke beech ek number socha hai.")

while True:
    guess = int(input("Guess karo: "))
    tries += 1

    if guess < secret:
        print("Ye kam hai, dobara koshish karo.")
    elif guess > secret:
        print("Ye zyada hai, dobara koshish karo.")
    else:
        print(f"Shabash! Aapne {tries} koshishon mein sahi guess kiya.")
        break
