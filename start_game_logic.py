import random

#######################################################################


def choose_table(player_1):
    choose_a_table = input("choose a table \n"
                         "press 2 for 2 players \n"
                         "press 3 for 3 players \n"
                         "press 4 for 4 players \n"
                         "press 5 for 5 players \n")

    if choose_a_table == "2":
        player_2 = [pick_a_random_player()]
        players = [player_1, player_2]
        print(players)
        return players

    if choose_a_table == "3":
        player_2 = [pick_a_random_player()]
        player_3 = [pick_a_random_player()]
        players = [player_1, player_2, player_3]
        print(players)
        return players

    if choose_a_table == "4":
        player_2 = [pick_a_random_player()]
        player_3 = [pick_a_random_player()]
        player_4 = [pick_a_random_player()]
        players = [player_1, player_2, player_3, player_4]
        print(players)
        return players

    if choose_a_table == "5":
        player_2 = [pick_a_random_player()]
        player_3 = [pick_a_random_player()]
        player_4 = [pick_a_random_player()]
        player_5 = [pick_a_random_player()]
        players = [player_1, player_2, player_3, player_4, player_5]
        print(players)
        return players

########################################################################################################################

def number_of_player():
    count_players = 0
    with open("player list.csv", "r") as my_file:
        for player in my_file:
            count_players += 1
        count_players = int(count_players) - 1
        return count_players


def make_a_random_number():
    amount_of_players = number_of_player()
    random_number = random.randint(1, amount_of_players)
    return random_number


def pick_a_random_player():
    all_players = []
    random_player_place_in_csv = int(make_a_random_number())

    with open("player list.csv", "r") as my_file:
        for player in my_file:
            all_players.append(player)
        return all_players[random_player_place_in_csv]

#######################################################################


# FIND OUT THE NUMBER THE PLAYERS
def count_the_players(table):
    count_players = 0
    for player in table:
        count_players += 1
    players = int(count_players)
    return(players)

#######################################################################


# DIVIDE CARDS AMONGST THE PLAYERS
def divide_cards_amongst_the_players(players, all_cards, player_1_deck, player_2_deck, player_3_deck, player_4_deck, player_5_deck):
    counter = 1
    card = 0
    while card < 52:

        # circle back to the first player
        if int(counter) > int(players):
            counter = 1

        elif counter == 1:
            popped_card = all_cards.pop(-1)
            player_1_deck.append(popped_card)
            counter += 1
            card += 1

        elif counter == 2:
            popped_card = all_cards.pop(-1)
            player_2_deck.append(popped_card)
            counter += 1
            card += 1

        elif counter == 3:
            popped_card = all_cards.pop(-1)
            player_3_deck.append(popped_card)
            counter += 1
            card += 1

        elif counter == 4:
            popped_card = all_cards.pop(-1)
            player_4_deck.append(popped_card)
            counter += 1
            card += 1

        elif counter == 5:
            popped_card = all_cards.pop(-1)
            player_5_deck.append(popped_card)
            counter += 1
            card += 1

    # throw away left over cards for 3 & 5-person game
    if players == 3:
        player_1_deck.pop(-1)

    if players == 5:
        player_1_deck.pop(-1)
        player_2_deck.pop(-1)

    return player_1_deck, player_2_deck, player_3_deck, player_4_deck, player_5_deck
##################################################


# PICK UP 5 CARDS INTO EVERY PLAYER'S HANDS
def take_cards_into_hand(player_deck):
    i = 0
    player_hand = []
    while i < 5:
        if player_deck == []:
            break
        else:
            popped_card = player_deck.pop(0)
            player_hand.append(popped_card)
            i += 1
    return player_hand

#######################################################################


def five_cards_for_each(players_cards):
    player_1_hand = take_cards_into_hand(players_cards[0])
    player_2_hand = take_cards_into_hand(players_cards[1])
    player_3_hand = take_cards_into_hand(players_cards[2])
    player_4_hand = take_cards_into_hand(players_cards[3])
    player_5_hand = take_cards_into_hand(players_cards[4])

    all_hands = [player_1_hand, player_2_hand, player_3_hand, player_4_hand, player_5_hand]
    print("in hand: ", all_hands[0], "in deck: ", players_cards[0])
    print("in hand: ", all_hands[1], "in deck: ", players_cards[1])
    print("in hand: ", all_hands[2], "in deck: ", players_cards[2])
    print("in hand: ", all_hands[3], "in deck: ", players_cards[3])
    print("in hand: ", all_hands[4], "in deck: ", players_cards[4])

    return all_hands

#######################################################################

# find all lowest cards of all the players


def find_lowest_card_in_all_hands(all_hands):
    lowest_cards = []
    for hand in all_hands:
        my_hand = hand
        result = find_lowest_card_in_single_hand(my_hand)
        lowest_cards.append(result[0])
        print("lowest cards in all hands",result)
    print("lowest cards", lowest_cards)
    return lowest_cards


def find_lowest_card_in_single_hand(hand):
    lowest_card = "x"
    min_val = 15
    for card in hand:
        card_split = card.split(" ")
        card_value = int(card_split[0])

        if min_val >= card_value:
            min_val = card_value
            lowest_card = card

    return min_val, lowest_card, hand

#######################################################################

# go over the list and see who has the lowest card

def compare_cards(lowest_cards):
    winning_card = 15
    for card in lowest_cards:
        if winning_card > card:
            winning_card = card
    print("winning card", winning_card)

# now go over the lowest card and compare it again to see if there are more cards with that value

    tie_set = [winning_card]
    for card in lowest_cards:
        if winning_card == card:
            tie_set.append(card)
    tie_set.pop()
    print("tie set", tie_set)
    return [tie_set, winning_card]

def check_amount_of_winning_set(compared_cards):
    number_of_players = 0
    for card in compared_cards:
        number_of_players += 1
    print("number_of_players", number_of_players)
    return number_of_players


def pick_a_player_to_start_game(tie_set, winning_card, lowest_cards):
    number_of_players = check_amount_of_winning_set(tie_set)

    for card in lowest_cards:
        if winning_card == lowest_cards[0]:
            print("player 1 starts")
            return 1

    if number_of_players == 1:
        for card in lowest_cards:

            if winning_card == lowest_cards[1]:
                print("player 2 starts")
                return 2
            if winning_card == lowest_cards[2]:
                print("player 3 starts")
                return 3
            if winning_card == lowest_cards[3]:
                print("player 4 starts")
                return 4
            if winning_card == lowest_cards[4]:
                print("player 5starts")
                return 5

    if number_of_players == 2:
        for card in lowest_cards:

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[2]:
                list_of_players = [2, 3]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[3]:
                list_of_players = [2, 4]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[4]:
                list_of_players = [2, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[2] and winning_card == lowest_cards[3]:
                list_of_players = [3, 4]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[2] and winning_card == lowest_cards[4]:
                list_of_players = [3, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[3] and winning_card == lowest_cards[4]:
                list_of_players = [4, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

    if number_of_players == 3:
        for card in lowest_cards:

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[2] and winning_card == lowest_cards[3]:
                list_of_players = [2, 3, 4]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[2] and winning_card ==lowest_cards[4]:
                list_of_players = [2, 3, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[3] and winning_card ==lowest_cards[4]:
                list_of_players = [2, 4, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player

            if winning_card == lowest_cards[2] and winning_card == lowest_cards[3] and winning_card ==lowest_cards[4]:
                list_of_players = [3, 4, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player


    if number_of_players == 4:
        for card in lowest_cards:

            if winning_card == lowest_cards[1] and winning_card == lowest_cards[2] and winning_card == lowest_cards[3] and winning_card == lowest_cards[4]:
                list_of_players = [2, 3, 4, 5]
                starting_player = random.choice(list_of_players)
                print("player", starting_player, "starts")
                return starting_player


