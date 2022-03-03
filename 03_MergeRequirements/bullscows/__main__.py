import sys
import os
import urllib.request
from .bullscows import gameplay

def parse_args():
    path = sys.argv[1]
    word_len = 5 if len(sys.argv) < 3 else int(sys.argv[2])
        
    return path, word_len

def get_dictionary(path, word_len):
    if os.path.exists(path):
        with open(path, "rt") as f:
            dictionary = f.read().splitlines()
    else:
        url_data = urllib.request.urlopen(path).read().decode()
        dictionary = url_data.splitlines()
    return list(filter(lambda w: len(w) == word_len, dictionary))

def inform(format_string, bulls, cows):
    print(format_string.format(bulls, cows))

def ask(prompt, valid=None):
    if valid is None:
        return input(prompt)

    while True:
        guess = input(prompt)
        if guess in valid:
            return guess

path, word_len = parse_args()
dictionary = get_dictionary(path, word_len)
attempts = gameplay(ask, inform, dictionary)

print(f"Попыток: {attempts}")
