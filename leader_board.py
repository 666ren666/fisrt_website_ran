from pprint import pprint


def find_top_player():
    with open("player list.csv", "r") as my_file:
        top_list = []
        all_list = []
# read from file & write to my_list
        for file_line in my_file:
            line = file_line.split(",")
            my_line = f"{line[0]},{line[1]},{line[2]}"
            all_list.append(my_line)

# find top 10 players in my list
        i = 0
        while i < 10:
            top_player_score = -1

# find top player in my list
            for player in all_list:
                split_line = player.split(",")
                score = split_line[0]
                player_score = int(score)

# update the top score
                if player_score > top_player_score:
                    top_player_score = player_score
                    my_player = player

# remove player from my_list & add him to top_list
            top_list.append(my_player)
            all_list.remove(my_player)
            i += 1

        for player in top_list:
            print(player)
        print()
    return
