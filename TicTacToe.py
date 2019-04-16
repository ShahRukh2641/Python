import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False    
               
    for row in game:
        if all_same(row):
            print(f"Palyer {row[0]} wins Horizontaly!!!")   
            return True    

#Diagonal

    diags2 = []    

    for col, row in enumerate(reversed(range(len(game)))):
        diags2.append(game[col][row])
    if all_same(diags2):
            print(f"Palyer {diags2[0]} wins Horizontaly!!!")
            return True

    diags = []

    for ix in range(len(game)):
        diags.append(game[ix][ix]) 
    if all_same(diags):
            print(f"Palyer {diags[0]} wins Horizontaly!!!")
            return True

#Vertical  
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
    if all_same(check):
            print(f"Palyer {check[0]} wins Horizontaly!!!")
            return True
    return False        



def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupaid! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] =player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False    

play = True
players = [1,2]
while play:
    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player is {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2):"))
            row_choice =  int(input("What row do you want to play? (0,1,2):"))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeeeeeee")        
                play =  False
            else:
                print("Not a valid answer")
                play = False    
#game_board(game,just_display=True)
#game_board(game,player=1, row=2,column=1,)
