import random
import string


lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special_character = string.punctuation
length = int(input("Enter the length: "))
done = False
password_list = []
my_password = None
while not done:
    print("1) Lower, \n"
          "2) Upper, \n"
          "3) Numbers, \n"
          "4) Special Characters, \n"
          "5) Lower + Upper, \n"
          "6) Lower + Numbers, \n"
          "7) Lower + Special characters, \n"
          "8) Lower + Upper + Numbers, \n"
          "9) Lower + Upper + Special characters, \n"
          "10) Lower + Upper + Special characters + Numbers, \n"
          "11) Upper + Numbers, \n"
          "12) Upper + Special Characters, \n"
          "13) Upper + Numbers + Special Characters, \n"
          "14) Numbers + Special Characters,")
    option = int(input("Enter A Number for one Options:"))
    if option == 1:
        for i in range(length):
            password_list.append(random.choice(lower))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 2:
        for i in range(length):
            password_list.append(random.choice(upper))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 3:
        for i in range(length):
            password_list.append(random.choice(numbers))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 4:
        for i in range(length):
            password_list.append(random.choice(special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 5:
        for i in range(length):
            password_list.append(random.choice(lower + upper))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 6:
        for i in range(length):
            password_list.append(random.choice(lower + numbers))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 7:
        for i in range(length):
            password_list.append(random.choice(lower + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 8:
        for i in range(length):
            password_list.append(random.choice(lower + upper + numbers))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 9:
        for i in range(length):
            password_list.append(random.choice(lower + upper + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 10:
        for i in range(length):
            password_list.append(random.choice(lower + upper + numbers + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 11:
        for i in range(length):
            password_list.append(random.choice(upper + numbers))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 12:
        for i in range(length):
            password_list.append(random.choice(upper + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 13:
        for i in range(length):
            password_list.append(random.choice(upper + numbers + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    elif option == 14:
        for i in range(length):
            password_list.append(random.choice(numbers + special_character))
        random.shuffle(password_list)
        # converting the list to string
        my_password = ("".join(password_list))
        done = True
    else:
        print("Invalid option")

print(my_password)
# password = ''
# print(random.sample(chars))
# password += ''.join(random.sample(chars))
