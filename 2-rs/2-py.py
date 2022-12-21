OUTCOME_SCORE = {
    'WIN': 6,
    'DRAW': 3,
    'LOSS': 0,
}

CHOICE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

MATCHUPS = {
    'A': ['Y', 'Z'],
    'B': ['Z', 'X'],
    'C': ['X', 'Y'],
}

calculate_score = lambda outcome, choice: OUTCOME_SCORE[outcome] + CHOICE_SCORE[choice]

def matchups(opponent, choice):
    if MATCHUPS[opponent][0] == choice:
        # win
        pass
    elif MATCHUPS[opponent][1] == choice:
        # loss
        pass
    else
        # draw