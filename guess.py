import random  

play_again = ''
while play_again != 'no':
    rand_number = random.randint(1, 100)
    attempts = 0
    #Inicia el juego 
    player_number = 0
    while player_number != rand_number: #para permitir que el juego continue hasta que el jugador adivine el numero
        player_number = input("Guess the number between 1 to 100: ")
        player_number = int(player_number)
        attempts += 1
        if player_number < rand_number:
            print("Too low! Try again")
        elif player_number > rand_number:
            print("Too high! Try again")
    print(f"Congratulations, you win in {attempts} attempts!")
    play_again = input('Do you want to play again? yes/no: ')
    print(f'{play_again}')
    while play_again != 'yes' and play_again !='no':
        print(f'{play_again} is not a valid option')
        play_again = input('Do you want to play again? yes/no: ')

    # haz un trim al play_again



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