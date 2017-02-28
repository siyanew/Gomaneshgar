import random

current_state = None
history = None
question_list = []
words_list = []


def init(cs,h):
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
    return random.choice(question_list)


def make_guess():
    return random.choice(words_list)


def has_any_point_for_direct():
    if current_state['n'] == 101:
        return True
    return False


def has_any_point_for_vanahesht():
    if current_state['n'] == 999:
        return True
    return False
