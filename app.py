import database

MENU_PROMPT = """-- Score Game App --

Please choose one of these options:

1) Add a score.
2) See all scores.
3) Find a score by name (case sensitive).
4) See which score is Highest score
5) Exit.

Your selection:"""




def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        print(user_input)
        if user_input == "1":
            prompt_add_new_score(connection)
        elif user_input == "2":
            prompt_see_all_scores(connection)
        elif user_input == "3":
            prompt_find_score(connection)
        elif user_input == "4":
            prompt_get_highest_score_for_scores(connection)
        else:
            print("Invalid input, please try again!")



def prompt_add_new_score(connection):
    name = input("Enter score name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (f for female m for male): ")
    score = int(input("Enter score (0-1000): "))

    database.add_score(connection, name, age, gender, score)



def prompt_see_all_scores(connection):
    scores = database.get_all_scores(connection)

    for score in scores:
        print(f"{score[1]} ({score[2]}) - {score[3].upper()} {score[4]}/1000")



def prompt_find_score(connection):
    name = input("Enter score name to find: ")
    scores = database.get_scores_by_name(connection, name)

    for score in scores:
        print(f"{score[1]} ({score[2]}) - {score[3].upper()} {score[4]}/1000")


def prompt_get_highest_score_for_scores(connection):
    best_score = database.get_highest_score_for_scores(connection)
    print(f"The best score is {best_score[1]}: {best_score[4]}")
    print()



menu()