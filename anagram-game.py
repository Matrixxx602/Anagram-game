# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

print('Program wybierze z puli jakieś słowo i zrobi z niego anagram, Twoim zadaniem będzie odgadnąć jakie to słowo.\n')

# Pula słów do wybrania przez program
WORDS = ('anagram', 'lotnisko', 'rzeczownik', 'wiolonczela', 'python',)
# Wybór słowa przez program
word = random.choice(WORDS)
correct = word
# Utworzenie anagramu
anagram = ''
while word:
    position = random.randint(0, len(word)-1)
    anagram += word[position]
    word = word[:position] + word[position+1:]
    
# Próba odgadnięcia słowa

answer = None
i = 0
j = 0
while answer != correct:
    i += 1
    if i > 3 and j < len(correct):
        print('Jeśli chciałbyś podpowiedz wpisz "tak", jeśli nie, naciśnij "ENTER"')
        hint = input()
        if hint == 'tak':
            j += 1
            print(f"Słowo to: {correct[:j]}")
        
    print(f'\nAnagram słowa to: {anagram}')
    answer = input("Zgadnij słowo: ")
    if answer != correct:
        print('Źle, spróbuj ponownie')
    else: print('Super, udało Ci się odgadnąć!')