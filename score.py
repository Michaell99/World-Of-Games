import Live


# Function for updating the user's score file according to his wins
def add_score(difficulty):
    score_file = open('static/score.txt', 'w+')
    current_score = score_file.read()
    points_of_winning = (difficulty * 3) + 5
    current_score += str(points_of_winning)
    score_file.write(current_score)
    score_file.close()

# Opening the score file, and saving the current cscore as a variable
