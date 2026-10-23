import unicodedata
import random
import os
import shelve
import hashlib

#analise e geração textual
filename = 'dr_jekyll.txt'
punc_list = ".;,-“’”:?—‘!()*"

def split_line(line):
    return line.replace('-', ' ').split()

def clean_word(word):
    return word.strip(punc_list).lower()

def get_unique_words(filename):
    unique_words = {}
    for line in open(filename, "r", encoding="utf-8"):
        for word in split_line(line):
            word = clean_word(word)
            unique_words[word] = 1

    return unique_words

unique_words = get_unique_words(filename)

def frequence_word(filename):
    word_counter = {}
    for line in open(filename, "r", encoding="utf-8"):
        for word in split_line(line):
            word = clean_word(word)
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
    return word_counter
word_counter = frequence_word(filename)
def second_element(t):
    return t[1]

def print_most_frequence(word_counter, n=5):
    items = sorted(word_counter.items(), key=second_element, reverse=True)
    str = ""
    for word, count in items[:n]:
        
        str += f"{word}:{count}, "
    return str

word_list = open('words.txt', 'r', encoding='utf-8').read().split()
valid_words = {}
for word in word_list:
    valid_words[word] = 1

def subtract(d1, d2):
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
    return result

diff = subtract(word_counter, valid_words)

singletons = []
for word, count in diff.items():
    if count == 1:
        singletons.append(word)
    
palavras_mais_frequentes = print_most_frequence(word_counter, 10)
# aleatória de palavras com base na frequência
words = list(word_counter)
weights = list(word_counter.values())
frase_aleatoria_sem_bigram = " ".join(random.choices(words, weights=weights, k=5))


#bigramas
bigram_counter = {}
def count_bigram(bigram):
    key = tuple(bigram)
    if key in bigram_counter:
        bigram_counter[key] += 1
    else:
        bigram_counter[key] = 1
window = []

def process_word(word):
    window.append(word)

    if len(window) == 2:
        count_bigram(window)
        window.pop(0)


for line in open(filename, "r", encoding="utf-8"):
    for word in split_line(line):
        word = clean_word(word)
        process_word(word)

bigrams = list(bigram_counter)
weights = list(bigram_counter.values())
random_brigrams = random.choices(bigrams, weights=weights, k=5)

for pair in random_brigrams:
    frase_aleatoria_com_bigram = " ".join(pair)

successor_map = {}
window = []

def add_bigram_makarov(bigram):
    first, second = bigram

    if first in successor_map:
        successor_map[first].append(second)
    else:
        successor_map[first] = [second]

def process_word_bigram(word):
    window.append(word)

    if len(window) == 2:
        add_bigram_makarov(window)
        window.pop(0)

for line in open(filename, "r", encoding="utf-8"):
    for word in split_line(line):
        word = clean_word(word)
        process_word_bigram(word)

word = random.choice(list(successor_map.keys()))
frase_aleatoria_com_bigram_makarov = ""
for i in range(5):
    successor = successor_map[word]
    word = random.choice(successor)
    frase_aleatoria_com_bigram_makarov += " " + word

