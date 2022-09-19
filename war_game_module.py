from module import Card, Player
from pprint import pprint
import random
from start_game_logic import count_the_players, divide_cards_amongst_the_players, five_cards_for_each, \
    find_lowest_card_in_all_hands, compare_cards, pick_a_player_to_start_game

############################################################################################################# GAME CLASS


class Game:

    def __init__(self, deck, player_info, bet):
        self.player_info = player_info
        self.deck = deck
        self.player_1_deck = []
        self.player_2_deck = []
        self.player_3_deck = []
        self.player_4_deck = []
        self.player_5_deck = []
        self.bet = bet

    def start_game(self, deck, table):
        deck.shuffle()
        all_cards = deck.to_list()
        players_in_game = count_the_players(table)
        players_cards = list(divide_cards_amongst_the_players(players_in_game, all_cards, self.player_1_deck,
                        self.player_2_deck, self.player_3_deck, self.player_4_deck, self.player_5_deck))
        players_hands = five_cards_for_each(players_cards)
        lowest_cards_in_all_hands = find_lowest_card_in_all_hands(players_hands)
        compared_cards = compare_cards(lowest_cards_in_all_hands)
        starting_player = pick_a_player_to_start_game(compared_cards[0], compared_cards[1], lowest_cards_in_all_hands)
        print(starting_player)
        return players_cards, players_hands, starting_player, players_in_game

    def game_logic(self):
        pass

        # pick card from hand

        # refill hands

        # throw 2 3 or 4 cards if you have the same numeral
        # take cards in to hands if you don't have the right card to put
        # opponents draw card (pick at random between optional cards)
        # skip player if he is out (if he won)
        # set up time of action and limit


########################################################################################################################

########################################################################################################################

######################################################################################################### CHECK WHO WINS

# while True:
#     if player_1_hand == []:
#         print("!!!YOU WIN!!!")
#
#         # print(self.player_info)
#         updated_score = int(self.player_info[0])
#         print(self.bet)
#         self.player_info[0] = updated_score
#         player_x = f"{self.player_info[0]},{self.player_info[1]},{self.player_info[2]}"
#         print(f"\n\nYou now have: {self.player_info[0]} coins\n")
#         return player_x
#
#     if opponents == {[], [], [], []}:
#         print("YOU LOSE :(")
#         # print(self.player_info)
#         updated_score = int(self.player_info[0]) + (self.bet * 3)
#         self.player_info[0] = updated_score
#         player_x = f"{self.player_info[0]},{self.player_info[1]},{self.player_info[2]}"
#         print(f"\n\nYou now have: {self.player_info[0]} coins\n")
#         return player_x


############################################################################################################# GAME LOGIC


########################################################################################################################




# check if someone finished their cards and take them out of the game

def get_keys_for_value(dictionary, value):
    players_out_of_game = []
    for key in dictionary:
        if dictionary[key] == value:
            players_out_of_game.append(key)
    return players_out_of_game

########################################################################################################################


def is_my_bet_an_int(player_1):

    # check for correct amount of coins
    while True:
        # check for correct input
        while True:

            print("     Press 1: to bet 1 coin \n"
                  "     Press 2: to bet 5 coins  \n"
                  "     Press 3: to bet 10 coins \n"
                  "     Press 4: to bet 50 coins \n"
                  "     Press 5: to bet 100 coins ")
            placed = input("How many coins would you like to bet?")

            if placed == "1":
                a_bet = 1
                break
            if placed == "2":
                a_bet = 5
                break
            if placed == "3":
                a_bet = 10
                break
            if placed == "4":
                a_bet = 50
                break
            if placed == "5":
                a_bet = 100
                break
            else:
                print("\nwrong input")
                continue

        if int(player_1[0]) - a_bet >= 0:
            return int(a_bet)

        if int(player_1[0]) - a_bet < 0:
            print("\nYou don't enough coins, Please try again\n")
            continue

        else:
            print("Wrong choice entered, Please try again\n")
            continue


def do_i_have_coins(player_1):
    if 0 >= int(player_1[0]):
        player_1[0] = int(player_1[0]) + 1000
        print("Your coins have been re-filled")



########################################################################################################################

#
# def choose_table(player_1):
#     choose_a_table = input("choose a table \n"
#                          "press 2 for 2 players \n"
#                          "press 3 for 3 players \n"
#                          "press 4 for 4 players \n"
#                          "press 5 for 5 players \n")
#
#     if choose_a_table == "2":
#         player_2 = [pick_a_random_player()]
#         players = [player_1, player_2]
#         print(players)
#         return players
#
#     if choose_a_table == "3":
#         player_2 = [pick_a_random_player()]
#         player_3 = [pick_a_random_player()]
#         players = [player_1, player_2, player_3]
#         print(players)
#         return players
#
#     if choose_a_table == "4":
#         player_2 = [pick_a_random_player()]
#         player_3 = [pick_a_random_player()]
#         player_4 = [pick_a_random_player()]
#         players = [player_1, player_2, player_3, player_4]
#         print(players)
#         return players
#
#     if choose_a_table == "5":
#         player_2 = [pick_a_random_player()]
#         player_3 = [pick_a_random_player()]
#         player_4 = [pick_a_random_player()]
#         player_5 = [pick_a_random_player()]
#         players = [player_1, player_2, player_3, player_4, player_5]
#         print(players)
#         return players
#
# ########################################################################################################################

# def number_of_player():
#     count_players = 0
#     with open("player list.csv", "r") as my_file:
#         for player in my_file:
#             count_players += 1
#         count_players = int(count_players) - 1
#         return count_players
#
#
# def make_a_random_number():
#     amount_of_players = number_of_player()
#     random_number = random.randint(1, amount_of_players)
#     return random_number
#
#
# def pick_a_random_player():
#     all_players = []
#     random_player_place_in_csv = int(make_a_random_number())
#
#     with open("player list.csv", "r") as my_file:
#         for player in my_file:
#             all_players.append(player)
#         return all_players[random_player_place_in_csv]

########################################################################################################################
