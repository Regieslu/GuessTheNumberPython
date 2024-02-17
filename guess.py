import random  

rand_number = random.randint(1, 100)
attempts = 0

#Inicia el juego 
while True: #para permitir que el juego continue hasta que el jugador adivine el numero
    player_number = input("Guess the number between 1 to 100: ")
    
    # Con 'exit' sale del juego el jugador
    if player_number.lower() == 'exit':
        print("Quitting the game.")
        break
    
    player_number = int(player_number)
    attempts += 1

    if player_number < rand_number:
        print("Too low! Try again")
    elif player_number > rand_number:
        print("Too high! Try again")
    else:
        print(f"Congratulations, you win in {attempts} attempts!")
        break

# Computer plays
number = int(input("Number? "))

attempts = 0
guess = 0

min = 1
max = 100
guess = random.randint(min, max)
while guess != number:
    # userInput = input(str(guess) + '?')
    print(f'GUESS: ==== {guess} =====')
    if guess < number:
        print(f'low')
        min = guess + 1
    elif guess > number:
        print(f'higher')
        max = guess - 1
    print(f'rangos {min} - {max}')
    attempts+=1
    guess = random.randint(min , max)
print(f'Number {guess} is correct')
print(f'Computer won in {attempts} attempts!')