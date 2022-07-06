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
print(wordlist)
