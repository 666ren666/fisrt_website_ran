from leader_board import find_top_player
from score_update import update_the_score

def play_quit_leaderboard(player_1, player_with_new_score):

    quit_or_play = ""
    while quit_or_play != "1" or quit_or_play != "2" or quit_or_play != "3":
        quit_or_play = (input("PRESS 1 TO PLAY ANOTHER ROUND\nPRESS 2 TO QUIT\nPRESS 3 FOR LEADER-BOARD"))


        # play again
        if quit_or_play == "1":
            break

        #quit playing
        if quit_or_play == "2":
            print(f"\n\nYou now have: {player_1[0]} coins\n")
            print("LEADER-BOARD\n")
            update_the_score(player_with_new_score)
            f = find_top_player()
            print("THANK YOU FOR PLAYING")
            return "end game"

        # show leader-board
        if quit_or_play == "3":
            print("\nLEADER-BOARD\n")
            update_the_score(player_with_new_score)
            f = find_top_player()
            continue

        # wrong input
        else:
            print("\nERROR!\nplease enter 1 / 2 or 3 :")
            continue
