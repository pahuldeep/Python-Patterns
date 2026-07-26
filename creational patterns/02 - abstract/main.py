# from environment import validate_age
# from environment import FrogWorld, WizardWorld, GameEnvironment

# def main():
#     name = input("Hello. What's your name? ")
#     valid_input = False
#     while not valid_input:
#         valid_input, age = validate_age(name)
        
#     game = { True: FrogWorld, False: WizardWorld }[age < 18]

#     environment = GameEnvironment(game(name))
#     environment.play()


# if __name__ == '__main__':
#     main()



from environment import validate_age
from environment import FrogWorld, WizardWorld, HumanWorld, GameEnvironment

def main():
    name = input("Hello. What's your name? ")
    
    # Keep asking until we get a valid age
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
        
    # Switch case (Match statement) to handle 3 environments
    match age:
        case age if age < 12:
            game_class = FrogWorld
        case age if 12 <= age < 18:
            game_class = WizardWorld
        case _:
            game_class = HumanWorld

    # Initialize the game with the selected class
    environment = GameEnvironment(game_class(name))
    environment.play()

if __name__ == '__main__':
    main()
