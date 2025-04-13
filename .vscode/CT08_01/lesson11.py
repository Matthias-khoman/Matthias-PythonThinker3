import random
# Exercise 1a
print(ord('A'))
print(ord('a'))

# Exercise 1b
# char = "A" 
# if 65 <= ord(char) <=90:
#     print("This is a uppercase case")

# Task 1: Generate a strong password
def generate_password(length: int = 12) -> str:
    if length < 12:
        print("Must be 12")
        return None
    password = ''
    for _ in range(length):
        char_type = random.choice(['upper', 'lower', 'digits', 'symbols'])
        if char_type == 'upper':
            password += chr(random.randint(65, 90))
        elif char_type == 'lower':
            password += chr(random.randint(97, 122))
        elif char_type == 'digits':
            password += chr(random.randint(48, 57))
        elif char_type == 'symbols':
            password += chr(random.randint(33, 47))
    return password

# Task 2: generate new user

user_db = {}

def create_new_user(user_db: dict) -> dict | None:
    new_user = input("Who do you want to add? ").strip().lower()
    if new_user in user_db:
        print('User already exists!!')
        return None
    else:
        password = generate_password()
        user_db[new_user] = password
        print(f'username: {new_user}')
        print(f'password: {password}')
        return user_db

# create_new_user(user_db)
# print(user_db)

# Task 3: Update password

def update_password(user_db: dict) -> dict | None:
    username = input('What is your username? ').strip().lower()
    password = input('What is your current password? ')
    if username in user_db:
        pass
    else:
        print('You are not here! ')
        return None
    if password in user_db[username]:
        new_password = generate_password()
        user_db[username] = new_password
        print(user_db)
        return user_db
    else:
        print('You are not here! ')
        return None
    
# update_password(user_db)

# Task 4: Login Status

def login(user_db: dict) ->bool:
    alleged_username = input('USERNAME: ').strip().lower()
    auth_status = False
    if alleged_username not in user_db:
        auth_status = False
        print('Unsucessful')
        return False
    alleged_password = input('PASSWORD: ').strip()
    if alleged_password in user_db[alleged_username]:
        print('Login Sucessful')
        return True
    else:
        auth_status = False
        print('Login Unsuccessful!')
        return False
    
# login(user_db)

# Task 5: View User Data

def view_user_data(user_db):
    if not user_db:
        print("No data found")
        return None
    print('Usernames and Passwords:')
    for user, password in user_db.items():
            print(f'{user}: {'*' * len(password)}')


# view_user_data(user_db)

while True:
    print('\nUsername and Password Manager')
    print("1. Create a New User")
    print("2. Update Password")
    print("3. Login")
    print("4. View Stored Usernames and Passwords")
    print("5. Exit")
    user_input = int(input("What do you want to do?"))
    if user_input == 1:
        create_new_user(user_db)
    elif user_input == 2:
        update_password(user_db)
    elif user_input == 3:
        login(user_db)
    elif user_input == 4:
        view_user_data(user_db)
    elif user_input == 5:
        print('Exiting...')
        break
    else:
        print('Invalid Input. Enter a number 1-5')