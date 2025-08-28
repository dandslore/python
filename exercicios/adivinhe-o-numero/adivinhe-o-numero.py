
#if num > num_secreto:
#    print("Ta muito grande. Escolhe um numero menor")
# elif: num < num_secreto:
#   print("Pequeno demais. Fala outro numero")
#else: 
#  print("acertô miseravi")

import random

print("Guess the number!")
print("Please, input your guess: ")

numero_secreto = random.randint(0, 100)

while True:
    guess = int(input())

    if guess > numero_secreto:
        print("Too big!")

    elif guess < numero_secreto:
        print("Too small!")

    else:
        print("YouWin!!")
        break
    