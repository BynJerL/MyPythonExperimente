# Number Guessing
import random
player_point = 0
player_attempt = 1

def game_start():
    global player_attempt
    global player_point
    global min_number
    global max_number
    global number_text
    min_number = 1
    max_number = 5
    number_text = ""
    
    for x in range(min_number,max_number+1):
        number_text += f"{x}  "
        
    
    print(f"\nAttempt # {player_attempt}\n{'-'*20 }\nGuess any number:\n{number_text}\n")
    # The change is up to you, just modify the min_number, max_number, and the print function exactly above this comment.
    
    correct_number = random.randint(min_number,max_number)
    
    chosen_number = int(input("Your number: "))
    
    print(f"The correct number: {correct_number}")
    
    if chosen_number == correct_number:
        player_point += 1
        print(f"You got (1) point.\nCurrent point: {player_point}\n")
        game_loop()
    elif (chosen_number != correct_number) and ((chosen_number > max_number) or (chosen_number < min_number)):
        player_point -= 1
        print(f"Your number is NOT among the choices! DISQUALIFIED!\nCurrent point: {player_point}\n")
        game_loop()
    else:
        player_point += 0
        print(f"Too bad!\nCurrent point: {player_point}\n")
        game_loop()

def game_loop():
    global player_attempt
    player_attempt += 1
    game_start()

def main():
    print("Let's play a game!")
    game_start()

main()