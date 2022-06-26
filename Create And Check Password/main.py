import requests
import hashlib
import string
import random
from itertools import product
import datetime as dt
from string import ascii_letters, digits, punctuation
from random import randint


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()[]")


def generate_random_password(length):
    # shuffling the characters
    random.shuffle(characters)
    # picking random characters from the list
    password_list = []
    for i in range(length):
        password_list.append(random.choice(characters))
    # shuffling the resultant password
    random.shuffle(password_list)
    # converting the list to string
    my_password = ("".join(password_list))
    return my_password


def Get_Score(get_password):
    print("Here is your a new Password : " + str(get_password))
    t = 0
    sung = []
    upper_case_letter = 0
    lower_case_letter = 0
    special_character = 0
    number = 0
    underscore = 0
    brackets = 0
    # Checking password length
    if len(get_password) > 8:
        t = t + 2
    else:
        sung.append("Length Should Be More Than 8")
    # Assigning score
    for i in get_password:
        if i.isdigit():
            number = 1
        if i.isupper():
            upper_case_letter = 1
        if i.islower():
            lower_case_letter = 1
        if i in ['!', '@', '#', '$', '%', '&', '[', ']', '(', ')']:
            special_character = 2
        if i == "_":
            underscore = 1
        if i in ['(', ')', '{', '}', '[', ']', '<', '>']:
            brackets = 2
    # strong password Suggestion
    if number == 0:
        sung.append("Add Numbers")
    if lower_case_letter == 0:
        sung.append("Add Lower Case Letters")
    if upper_case_letter == 0:
        sung.append("Add Upper Case letters")
    if special_character == 0:
        sung.append("Add Special Character ! @ # $ % &")
    if underscore == 0:
        sung.append("Add Underscore")
    if brackets == 0:
        sung.append("Add Brackets ( ) { } [ ] < >")
    return sung, (t + number + upper_case_letter + lower_case_letter + special_character + underscore + brackets)


def request_api_data(query_char):
    ur1 = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(ur1)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the api and try again')
    return response


def get_password_leaks_counter(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, counter in hashes:
        if h == hash_to_check:
            return counter
    return 0


def pwned_api_check(check_password):
    # check password if exists in API response
    sha512_password = hashlib.sha1(check_password.encode('utf-8')).hexdigest().upper()
    first_five_char, tail = sha512_password[:5], sha512_password[5:]
    response = request_api_data(first_five_char)
    return get_password_leaks_counter(response, tail)


def checker_password(your_password):
    count = pwned_api_check(your_password)
    if count:
        return f"              The password you entered is: \n" \
               f"              ( {your_password} ) was found ( {count} ) \n" \
               f"              times... you should probably \n" \
               f"              change your password!"
    else:
        return f"             ( {your_password} ) was not found Carry on!"


guess = ""


def guess_password(your_password):
    global guess
    while guess != your_password:
        guess = ""
        # generating random passwords using for loop
        for letter in range(len(your_password)):
            guess_letter = characters[randint(0, 76)]
            guess = str(guess_letter) + str(guess)
        # print(guess)


def tryPassword(user_password, passwordSet):
    start = dt.datetime.now()
    attempts = 0
    for passcode in product(ascii_letters + digits + punctuation, repeat=len(user_password)):
        letters = "".join(passcode)
        attempts += 1
        if letters == passwordSet:
            end = dt.datetime.now()
            distance = end - start
            return attempts, distance


# what_do_you_want = input(
#     f"Do you want to create a password or check your own password \n"
#     f"If you want to create password enter 'create password' or 'change password' \n"
#     f"And follow the instructions \n"
#     f"Or if you want to check your own password, \n"
#     f"how many times has it been hacked? enter 'check password': ")
#
#
# if what_do_you_want == 'create password' or what_do_you_want == 'change password':
#     try:
#         length_password = int(input("Please enter the password length you want and we will create a password for you: "))
#     except ValueError:
#         print(f"please enter a number not letters")
#     my_new_password = generate_random_password(length_password)
#     suggestion, score = Get_Score(my_new_password)
#     if score <= 3:
#         print("Strength: The password is weak, do you want another password?")
#     elif 6 >= score > 3:
#         print("Strength: The password is Medium, it's good but not strong enough")
#     elif score >= 7:
#         print("Strength: The password is Strong")
#     if score >= 8:
#         print("Status: Valid Password")
# elif what_do_you_want == 'check password':
#     your_own_password = input("Enter your own password: ")
#     check_your_own_password = checker_password(your_own_password)
#     print(check_your_own_password)
#     tries, timeAmount = tryPassword(your_own_password, your_own_password)
#     print("Your password is found: ", guess)
#     print(f'Number of Tries: {tries}')
#     print(f'Time to hacking password: {timeAmount}')
# else:
#     print("please enter one of them {create password} or {check password}")

