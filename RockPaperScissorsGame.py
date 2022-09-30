# Rock Paper Scissors
import random
player_score = 0
player_start_turn = 1

def game_start():
    global player_score
    global player_turn
    global choices
    available_choices = ("rock","paper","scissors")
    
    print(f"\nTurn #{player_turn}\n{'—'*40}\nRock\t\tPaper\t\tScissors\n")
    
    player_choice = str(input("Your choice: "))
    random_computer_choice = random.choice(available_choices)
    print(f"Computer's choice: {random_computer_choice.capitalize()}")
    
    if player_choice.lower() in available_choices:
        if ((player_choice.lower() == 'paper') and (random_computer_choice == 'rock')) or ((player_choice.lower() == 'rock') and (random_computer_choice == 'scissors')) or ((player_choice.lower() == 'scissors') and (random_computer_choice == 'paper')):
            player_score += 1
            print(f"\nYou Win! ヾ(＾-＾)ノ\n\nCurrent score: {player_score}\n")
            game_loop()
        
        elif player_choice.lower() == random_computer_choice:
            player_score += 0
            print(f"Tie! ಠಿ_ಠ\n\nCurrent score: {player_score}\n")
            game_loop()
        
        else:
            player_score += -1
            print(f"\You Lose! ಥ‿ಥ\n\nCurrent score: {player_score}\n")
            game_loop()
    else:
        player_score += -1
        print(f"Wait, that's a wrong input! ( ͡° ʖ̯ ͡°)\n\nCurrent score: {player_score}\n")
        game_loop()    

def game_loop():
    global player_turn
    player_turn += 1
    game_start()

def main():
    global player_start_turn
    global player_turn
    player_turn = player_start_turn
    
    greetings = f"~ Let's Play a Game: Rock Paper Scissors ~ \n{'—[]'*14+'—'}"
    print(greetings)
    
    game_start()
    
main()
