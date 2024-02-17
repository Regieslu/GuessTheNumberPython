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
low = 1
high = 100
computer_guess = random.randint(1, 100)
print(f'Computer player, enter your guess: {computer_guess}')
attempts+=1
while computer_guess!= rand_number:
    if computer_guess < rand_number:
        print('Computer guessed too low! Try again')
        low = computer_guess + 1
    else:
        print('Computer guessed too high! Try again')
        high = computer_guess - 1
        break
computer_guess = random.randint(low, high)
print(f'Computer player, enter your guess: {computer_guess}')
attempts += 1
print(f"Computer won in {attempts} attempts!")
