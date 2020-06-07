import random
import requests
import tokenize
import re
from letter_translator import LETTER_TRANSLATOR
from password_generator import swap_symbols, make_password_from_line, random_char
import os

PASSWORD_LENGTH = 15

def main():
        book_num = str(random.randint(10000,33000))
        book_filename = get_book_file(book_num)

        print(book_filename)

        words = get_words_from_book(book_filename)

        if words is None:
            remove_book(book_filename)
            quit()

        print(words)

        password = make_password_from_line(words, PASSWORD_LENGTH)
        print(password)

def remove_book(book_filename):
    os.remove(book_filename)

def get_info(info, f):
    line = f.readline()

    while info not in line:
        line = f.readline()
    
    return line[len(info)+2:-1]

def get_book_file(book_num):
    book_url = f"http://www.gutenberg.org/cache/epub/{book_num}/pg{book_num}.txt"

    req = requests.get(book_url, allow_redirects=True)

    book_filename = f"book{book_num}.txt"

    with open(book_filename, 'wb') as f:
        f.write(req.content)
    
    return book_filename

def get_words_from_book(book_filename):
    with open(book_filename, 'r') as f:
        line = str(f.readline())

        if "DOCTYPE HTML PUBLIC" in line:
            print("No book available at this address.")
            return None

        title = get_info("Title", f)
        author = get_info("Author", f)
        language = get_info("Language", f)

        if "English" not in language:
            print("Non-English title")
            return None

        f.seek(5000)

        try:
            text_selection = f.readline()
            
            while text_selection == "\n" or len(text_selection) < 70:
                text_selection = readline() 

            print(text_selection)
        except:
            pass

        words = re.split(" ", text_selection)
        return words

if __name__ == "__main__":
    main()
