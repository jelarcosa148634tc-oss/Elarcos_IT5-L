print ("Hello, World!")


# === Random rani sir na code ===
import random
import string
import time


def generate_random_password(length=12):
    """Generates a strong, random password containing letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def guess_the_number():
    """A quick mini-game where the computer picks a number and you try to guess it."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🤖 I'm thinking of a number between 1 and 100.")

    simulated_guesses = [50, 75, secret_number]

    for guess in simulated_guesses:
        time.sleep(0.5)
        attempts += 1
        print(f"👤 Player guesses: {guess}")

        if guess < secret_number:
            print("📈 Too low!")
        elif guess > secret_number:
            print("📉 Too high!")
        else:
            print(
                f"🎉 Correct! The number was {secret_number}. Found in {attempts} attempts."
            )
            break


print("--- Random Password Generator ---")
print(f"Generated Password: {generate_random_password()}\n")

print("--- Game Simulation ---")
guess_the_number()
