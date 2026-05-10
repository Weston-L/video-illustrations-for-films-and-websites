import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Read the first names from the file
with open('firstnames.txt', 'r') as file:
    first_names = [line.strip() for line in file]

# Read the last names from the file
with open('lastnames.txt', 'r') as file:
    last_names = [line.strip() for line in file]

# Find the maximum length of first name and last name combination
max_length = max(len(f"{first_name} {last_name}") for first_name, last_name in zip(first_names, last_names))

while True:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    password_length = random.randint(8, 16)  # Random length between 8 and 16 characters
    password = generate_random_password(password_length)
    
    # Print with padding to align "password" under each other
    print(f"{first_name} {last_name}{(' ' * (max_length - len(f"{first_name} {last_name}")))} - password: {password}")
    
    if input().lower() == 'q':
        break
