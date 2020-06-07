import random

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


def build_password(word_dict, simple=True):
    dict_section = word_dict[str(random.randint(2,8))]
    password = dict_section[random.randint(0, len(dict_section)-1)]
    used_words = []

    while len(password) < PASSWORD_LENGTH:
        dict_section = word_dict[str(random.randint(2,8))]
        new_word = dict_section[random.randint(0, len(dict_section)-1)]

        if simple:
            password = password + random_char(len(new_word) % 2 == 0)

        if not new_word in used_words:
            password = password + new_word
            used_words.append(new_word)

    return password


def make_password_from_line(words, password_length):
    try:
        phrase_position = random.randint(1, len(words)-8)

        password = words[phrase_position]

        phrase_position = phrase_position + 1
        while len(password) < password_length:
            password = password + variability_symbol() + words[phrase_position]

            phrase_position = phrase_position + 1

        return password + variability_symbol()

    except ValueError:
        password = ""

        for i in range(1, len(words)):
            password = password + words[i] + variability_symbol()
        
        while len(password) < password_length:
            password = password + variability_symbol()

            if len(password) >= password_length:
                break

        return sanitize_password(password + random_char(False))


def variability_symbol():
    do_add_symbol = (random.randint(0, 10)) % 2 == 0

    if do_add_symbol:
        use_longer_range = (random.randint(0, 10)) % 2 == 0

        return random_char(use_longer_range)
    else:
        return ""


def sanitize_password(password):
    clean_password = ""

    for i in range(len(password)):
        if password[i] != "\n":
            clean_password = clean_password + password[i]

    return clean_password

def random_char(use_range_with_numbers=True):
    if use_range_with_numbers:
        random_num = random.randint(42, 64)
        random_num = random_num if random_num != 34 else 33 #avoid punctuation marks
        return chr(random_num)
    else:
        return chr(random.randint(33, 38))
