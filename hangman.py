import random
import subprocess
import gallow

def draw_screen(known, mistakes):
    subprocess.call("clear")
    gallow.draw(mistakes)
    buff = ""
    for n in known:
        buff += n
        buff += " "
    print(buff)

subprocess.call("clear")
print("Choose your difficulty:")
print("(1) Low (Cowardly, but a safe bet.)")
print("(2) Medium (Living on the edge?)")
print("(3) High (Suicidal, are we?)")
print("(4) Custom (Oh no.)")
difficulty = int(input("-> "))

if difficulty == 1:
    f =  open('easy', 'r')
    wordlist =f.read().split('\n')
if difficulty == 2:
    f =  open('medium', 'r')
    wordlist =f.read().split('\n')
if difficulty == 3:
    f =  open('hard', 'r')
    wordlist =f.read().split('\n')
if difficulty == 4:
    f =  open('custom', 'r')
    wordlist =f.read().split('\n')

mistakes = 0
word = random.choice(wordlist)
length = len(word)
known = ""
while length > 0:
    known += "_"
    length -= 1

while mistakes < 9:
    draw_screen(known, mistakes)
    if known == word:
        print("You win!")
        break
    guess = input("Guess a letter/word: ")
    if len(guess) == 1:
        if guess in word:
            matches = []
            for pos, char in enumerate(word):
                if char == guess:
                    matches.append(pos)
            for match in matches:
                known = known[0:match]+guess+known[match+1: ]
        else:
            mistakes += 1
    else:
        if guess == word:
            known = word
        else:
            mistakes += 1
if known != word:
    draw_screen(known, mistakes)
    print("You lose!")
