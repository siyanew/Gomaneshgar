import random

current_state = None
history = None
question_list = []
words_list = []


def inits(cs,h):
    global current_state
    global history
    current_state = cs
    history = h
    f = open("data/questions.txt",encoding="UTF-8")
    question_list.extend(f.read().split("\n"))
    f.close()
    f = open("data/words.txt",encoding="UTF-8")
    words_list.extend(f.read().split("\n"))
    f.close()


def choose_question():
    # Just Choose a Random Question
    return random.choice(question_list)


def make_guess():
    # Just Choose a Random Answer
    return random.choice(words_list)


def has_any_point_for_direct():
    # It's jsut for test and Debug and called in 101st question
    if current_state['n'] == 101:
        return True
    return False


def has_any_point_for_vanahesht():
    # It's jsut for test and Debug and called in 999th question
    if current_state['n'] == 999:
        return True
    return False
