def rock_paper_scissors():
    play = True
    game_live = True
    player1 = 0
    player2 = 0
    round = 0
    while play == True:
        choice = input()
        if choice == "End":
            if game_live:
                round += 1
                game_live = False
                if player1 > player2:
                    print("Contest #" + str(round) + ": Player 1 wins")
                elif player2 > player1:
                    print("Contest #" + str(round) + ": Player 2 wins")
                else:
                    print("Contest #" + str(round) + ": Tie")
                player1 = 0
                player2 = 0
            else:
                play = False
                return
        else:
            if choice[0] == choice[1]:
                pass
            elif choice[0] == "R" and choice[1] == "S":
                player1 += 1
            elif choice[0] == "S" and choice[1] == "P":
                player1 += 1
            elif choice[0] == "P" and choice[1] == "R":
                player1 += 1
            else:
                player2 += 1
            game_live = True

rock_paper_scissors()