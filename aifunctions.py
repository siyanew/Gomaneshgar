current_state = None
history = None
question_list = []
words_list = []


def init(cs,h):
    global current_state
    global history
    current_state = cs
    history = h
    # Initialize Everything You Want


def choose_question():
    # Here You Should Implement Your AI to Prepare the next question
    return "آیا از شاعران است؟"


def make_guess():
    # This method return a guess
    return "سعدی"


def has_any_point_for_direct():
    # If it is true , The bot will message a Direct Question
    return False


def has_any_point_for_vanahesht():
    # If this Method return True it will send make_guess() as vanahesht
    return False
