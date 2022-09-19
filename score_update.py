####################################################################################### UPDATE SCORE IN PLAYER-LIST FILE

def update_the_score(player_with_new_score):

    list_of_all_players = []

    player_with_new_score = str(player_with_new_score)
    player_string = player_with_new_score.split(",")
    temp_player_score_updated = f"{player_string[0]},{player_string[1]},{player_string[2]},"

    # add your player to list
    list_of_all_players.append(temp_player_score_updated + "\n")

    # add all players EXCEPT your player in csv to list
    with open("player list.csv", "r+") as all_the_players:
        for player in all_the_players:
            temp_list = str(player)
            temp = temp_list.split(",")
            if temp[1] == player_string[1] and temp[2] == player_string[2]:
                continue
            list_of_all_players.append(player)

    # over-write csv with updated score
    with open("player list.csv", "w") as updated_file:
        first_row = "score,user_name,password"
        for player in list_of_all_players:
            temp_line = str(player)
            updated_file.writelines(temp_line)
