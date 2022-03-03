import textdistance
import random

def bullscows(guess, secret):
    
    bulls = textdistance.hamming.similarity(guess, secret)
    cows = textdistance.bag.similarity(guess, secret)
    return bulls, cows

def gameplay(ask, inform, words):

    secret = random.choice(words)
    attempts = 0
    while True:
        guess = ask("Введите слово: ", words)
        attempts += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        
        if guess == secret:
            break

    return attempts
