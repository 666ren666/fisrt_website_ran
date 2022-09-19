from login_signin import choose_between_login_and_signin
from module import Deck, Table
from war_game_module import Game, is_my_bet_an_int, do_i_have_coins
from start_game_logic import choose_table, pick_a_random_player
from play_quit_leaderboard import play_quit_leaderboard



# pick_a_random_player()

# CHOOSE BETWEEN : SIGN IN & LOG IN
player_1 = choose_between_login_and_signin()

print(f"\n\n\nHello {player_1[1]} \nYou have: {player_1[0]} coins")
start_game = input("PRESS ENTER TO START")

# chooses how many players are playing
my_table = choose_table(player_1)

# pick who starts the game



while True:

    # PLACE YOUR BET
    bet = is_my_bet_an_int(player_1)
    player_1[0] = int(player_1[0]) - bet
    # CHECK IF PLAYER IS OUT OF COINS, IF SO: ADD 1000 COINS TO PLAYER
    do_i_have_coins(player_1)

    # INITIALIZE THE GAME
    my_deck = Deck()
    table = Table(my_deck, my_table)
    card_game = Game(my_deck, my_table, bet)

    # START GAME & UPDATE COINS IN CSV FILE
    player_with_new_score = card_game.start_game(my_deck, my_table)

    # CHOOSE BETWEEN : PLAY / QUIT or LEADER-BOARD
    a = play_quit_leaderboard(player_1, player_with_new_score)
    if a == "end game":
        break
