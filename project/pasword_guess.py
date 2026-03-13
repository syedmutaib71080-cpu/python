import random

easy_passwords = ['password', 'cake', 'king', 'hello', 'apple']

medium_passwords = ['shipment', 'Admin', 'Welcome', 'kingmaker', 'kinght']

hard_passwords = ['wiseperson', '5trongpassed', 'complementthing', 'securitycheck', 'randomthings']

print("Welcome to the password guess game!")
print("You will have to guess the password in order to win the game.")
print("There are three difficulty levels: easy, medium, and hard.")
print("Easy passwords are common and easy to guess, medium passwords are a bit more difficult, and hard passwords are very difficult to guess.")    
level = input("Please choose a difficulty level (easy, medium, hard): ").lower()
if level =="easy":
    secret= random.choice(easy_passwords)
elif level == "medium":
    secret = random.choice(medium_passwords)
elif level == "hard":
    secret = random.choice(hard_passwords)
else:    
    print("Invalid difficulty level. defaulting to easy.")
    secret = random.choice(easy_passwords)
attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ")
    attempts += 1
    if guess == secret:
        print(f"Congratulations! You've guessed the password '{secret}' in {attempts} attempts!")
        break
    
    hint = ""
    
    for i in range( len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
        
    print(f"Hint: {hint}")
    
print("Thanks for playing the password guess game!")