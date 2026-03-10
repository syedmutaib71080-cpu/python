import random

subjects = ["The cat", "A dog", "The president", "A scientist", "An alien"]
verbs = ["eats", "jumps over", "finds", "creates", "destroys"]
objects = ["a mouse", "a fence", "a new element", "a spaceship", "a city"]

while True:
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    fake_news = f"BREAKING NEWS: {subject} {verb} {object}."
    print(f"\n{fake_news}")
    user_input = input("Do you want to generate another fake news? (yes/no): ").strip().lower()
    if user_input == "no":
        print("Goodbye!")
        break
    
print("\nThank you for using the Fake News Generator!")