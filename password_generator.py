import random
from common import SYMBOLS

def swap_symbols(password):
    new_password = ""
    for i in range(len(password)):
        if i % 3 == 0:
            try:
                new_password = new_password + LETTER_TRANSLATOR[password[i]]
            except:
                new_password = new_password + password[i]
        else:
            new_password = new_password + password[i]
    return new_password


def make_password_from_line(words, password_length):
    contains_symbol = False
    contains_capital = False
    contains_number = False
    
    try:
        phrase_position = random.randint(1, len(words)-8)

        password = words[phrase_position]

        phrase_position = phrase_position + 1
        while len(password) < password_length:
            password, contains_symbol, contains_capital, contains_number = add_word_to_password(
                password, 
                words[phrase_position], 
                contains_symbol, 
                contains_capital, 
                contains_number
            )

            phrase_position = phrase_position + 1

        return password

    except ValueError:
        password = ""

        for i in range(1, len(words)):
            password,contains_symbol, contains_capital, contains_number = add_word_to_password(
                password, 
                words[phrase_position], 
                contains_symbol, 
                contains_capital, 
                contains_number
            )

            if len(password) >= password_length:
                break
            
        while len(password) < password_length:
            password = password + variability_symbol()

            if len(password) >= password_length:
                break

        return sanitize_password(password + variability_symbol())

def add_word_to_password(password, word, contains_symbol, contains_capital, contains_number):
    do_add_capital = get_random_bool()
    word_to_add = (word if do_add_capital else add_capital_letter(word))
    print(f"Adding {word_to_add} to password")
    symbol_to_add, symbol_type = variability_symbol()

    contains_symbol = contains_symbol or (symbol_type == "SYMBOL")
    contains_capital = contains_capital or do_add_capital
    contains_number = contains_number or (symbol_type == "NUMBER")

    password = password + symbol_to_add + word_to_add
    
    return password, contains_symbol, contains_capital, contains_number

def get_random_bool():
    return random.randint(0,10) % 2 == 0

def variability_symbol():
    do_add_symbol = get_random_bool()

    if do_add_symbol:
        return SYMBOLS[random.randint(0, len(SYMBOLS)-1)], "SYMBOL"
    else:
        return str(random.randint(0,9)), "NUMBER"


def sanitize_password(password):
    clean_password = ""

    for i in range(len(password)):
        if password[i] != "\n":
            clean_password = clean_password + password[i]

    return clean_password


def add_capital_letter(password):
    print("Capitalizing " + password)
    
    if len(password) == 1:
        return password.upper()
    else: 
        return password[0].upper() + password[1:len(password)]


def add_number(password):
    pass

def add_symbol(password):
    pass

# VALID SYMBOLS 33, 35-38, 42-47, 58-64
# OMIT 34, 39, 40, 41
# NUMBERS 48-57

# !@#$%^&*-+_.<>?;:=
