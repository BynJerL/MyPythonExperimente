# {My own game}
# Future Update Plan: Money
# Default Money : 100 RPS

# Food/drink prices:
# (1) Bread = 25 RPS
# (2) Pie = 50 RPS
# (3) Shortcake = 40 RPS
# (4) Fish 'n Chips = 75 RPS
# (5) Tea = 10 RPS
# (6) Coffee = 15 RPS
# (7) Milk = 15 RPS
# ... (coming soon)

print("A simple game\n")
print("You are starving, and you come to TheCafe.\n")

answer = input("Would you like to buy something here? (yes/no) ").lower().strip()

if answer == "yes":
    print("")
    answer = input("What things you wanna buy? (food/drink) ").lower().strip()
    
    if answer == "food":
        print("\nHere's the menu: (bread/shortcake/pie/fish 'n chips')")
        answer = input("Pick one ").lower().strip()
        
        if answer == "bread":
            print("\nYou've bought a bread")
            answer = input("Do you want to eat it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou ate the bread.")
                print("Your energy restored quite a lot.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
            
        elif answer == "shortcake":
            print("\nYou've bought a shortcake")
            answer = input("Do you want to eat it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou ate the shortcake.")
                print("Your energy restored a lot, and you're happy.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
                
        elif answer == "pie":
            print("\nYou've bought a pie")
            answer = input("Do you want to eat it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou ate the pie.")
                print("Your energy restored quite a lot, and you're happy.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
                
        elif answer == "fish 'n chips":
            print("\nYou've bought a plate of fish 'n chips")
            answer = input("Do you want to eat it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou ate the plate of fish 'n chips.")
                print("Your energy restored a lot, and you're happy.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
        else:
            print("Invalid input!")
            
    elif answer == "drink":
        print("\nHere's the menu: (tea/coffee/milk)")
        answer = input("Pick one ").lower().strip()
        
        if answer == "tea":
            print("\nYou've bought a glass of tea")
            answer = input("Do you want to drink it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou drink the tea.")
                print("Your energy restored a little, and you're happy.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
        elif answer == "coffee":
            print("\nYou've bought a glass of coffee")
            answer = input("Do you want to drink it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou drink the coffee.")
                print("Your energy restored a lot.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
        elif answer == "milk":
            print("\nYou've bought a glass of milk")
            answer = input("Do you want to drink it? (yes/no) ").lower().strip()
            
            if answer == "yes":
                print("\nYou drink the milk.")
                print("Your energy restored quite a lot.")
            elif answer == "no":
                print("\n...\nYour energy is drained.")
            else:
                print("Invalid Input")
        else:
            print("Invalid input!")
            
    else:
        print("Invalid input!")

else:
    print("That's too bad!")

print("The End")
