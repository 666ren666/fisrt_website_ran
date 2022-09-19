

def choose_between_login_and_signin():
    choice = ""
    while choice != "1" or choice != "2":
        choice = input("press 1 to sign in:\npress 2 to log in:")

        if choice == "1":
            a_player = sign_in()
            return a_player

        if choice == "2":
            a_player = log_in()
            return a_player

        else:
            print("Wrong input")
            continue

################################################################################################################ SIGN-IN


def sign_in():
    while True:
        a = "player not found"
        print("SIGN IN BELOW:")
        user_name = input("what is your name:")
        password = input("pick a password")
        score = 1000
        player = f"{score},{user_name},{password},\n"

        # CHECK IF USER-NAME IS TAKEN
        a = check_if_username_is_taken(user_name)

        # TRY AGAIN
        if a == "player found":
            print("\nThis name is already taken, Please try another one")
            continue

        # UPDATE PLAYER IN CSV FILE & return player
        else:
            update_csv_file_with_new_player(player)
            player_1 = [score, user_name, password]
            return player_1


def check_if_username_is_taken(user_name):
    with open("player list.csv", "r") as all_players:
        for player in all_players:
            my_player = player.split(",")

            if user_name == my_player[1]:
                return "player found"


def update_csv_file_with_new_player(player):
    with open("player list.csv", "r+") as all_players:
        all_players.readlines()
        all_players.writelines(player)
        all_players.close()


################################################################################################################# LOG-IN


def log_in():
    while True:
        a = ""
        print("LOG IN BELOW:")
        user_name = input("input user-name:")
        password = input("input pass-word")

        a = check_if_player_exists_in_csv_file(user_name, password)
        # PLAYER FOUND, PICK PLAYER & RETURN PLAYER

        if a == "player found":
            with open("player list.csv", "r") as all_players:
                for player in all_players:
                    my_player = player.split(",")

                    if user_name == my_player[1] and password == my_player[2]:
                        score = my_player[0]
                        player_1 = my_player
                        return player_1

        # PLAYER NOT FOUND & TRY AGAIN
        else:
            print("\nWrong user-name or password: Please try again")
            continue


def check_if_player_exists_in_csv_file(user_name, password):
    with open("player list.csv", "r") as all_players:
        for player in all_players:
            my_player = player.split(",")

            if user_name == my_player[1] and password == my_player[2]:
                return "player found"

            else:
                continue
