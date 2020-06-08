from common import SYMBOLS

def validate_password(password):
    has_capital_letter = False
    has_symbol = False
    has_number = False

    for i in range(len(password)):
        if is_capital_letter(password[i]):
            has_capital_letter = True
        elif is_symbol(password[i]):
            has_symbol = True
        elif is_number(password[i]):
            has_number = True
    
    return has_capital_letter, has_symbol, has_number

def is_capital_letter(char):
    return chr(char) >= 65 and chr(char) <= 90

def is_symbol(char):
    return chr(char) in SYMBOLS

def is_number(char):
    return chr(char) >= 48 and chr(char) <= 57