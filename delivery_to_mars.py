import random

def run_game():
    # Introduction:
    print('Welcome to Delivery to Mars! 🚀\n')
    print("It is the year 2156, and Elon Musk's idea came true...")
    print('There are already colonies on Mars!!!\n')
    print('Your mission is to complete deliveries from Earth to Mars.')
    print('Rockets have enough fuel for 100 days, and you start with 3 rockets.\n')
    print("Earn 8 rockets to win! Lose them all, and it's game over!\n")

    # Initial game state
    rockets = 3
    delivery_options = {
        1: {"distance": 30, "deviation_threshold": 30},
        2: {"distance": 45, "deviation_threshold": 20},
        3: {"distance": 60, "deviation_threshold": 10},
    }

    while rockets > 0:
        # Delivery type selection
        print('Choose a delivery type:')
        print('1 - Small (30 days)')
        print('2 - Medium (45 days)')
        print('3 - Large (60 days)')
        
        selection = int(input('Type: '))
        if selection not in delivery_options:
            print('❌ Invalid choice. Try again.\n')
            continue

        rocket_fuel = 100
        delivery = delivery_options[selection]
        distance = delivery["distance"]
        deviation_threshold = delivery["deviation_threshold"]

        print(f'\nThis delivery will take {distance} days.\n')

        # Possible deviation event
        deviation = random.randint(1, 115)
        if deviation >= deviation_threshold:
            print('👀 ..it seems there is a meteor shower, or maybe a solar flare, or a fuel leak..')
            print('Your rocket will have to make a deviation..\n')
            print('🧐 Proceed without deviation (1) or with deviation (2)?')
            
            choice = int(input('Choose: '))
            if choice == 2:
                rocket_fuel -= deviation
                print(f'Your rocket has fuel left for {rocket_fuel} days..\n')
            elif choice == 1:
                extra_loss = random.randint(1, 150)
                rocket_fuel -= extra_loss
                print(f'🖕 Proceeding without deviation costs {extra_loss} extra days of fuel.\n')
            else:
                print('❌ Invalid choice. Try again.\n')
                continue

        # Delivery outcome
        if rocket_fuel < distance:
            rockets -= 1
            print('😭 Ooops! You lost a rocket.\n')
        else:
            rockets += 1
            print('😎 Delivery successful! You earned one rocket!\n')

        print(f'Total rockets: {rockets}\n')

        if rockets == 0:
            print('💀 Game over! You ran out of rockets.')
        elif rockets == 1:
            print('😱 Only 1 rocket left..')
        elif rockets == 7:
            print('👽 Almost there.. Just one more!')
        elif rockets == 8:
            print('🎉 You won! Congratulations! 🥳')
            break

run_game()
