import asyncio
import copy

from bot import config, set_step, delete_step, get_data_step, current_state, history, vanahesht, set_twenty
from aifunctions import has_any_point_for_vanahesht, make_guess, has_any_point_for_direct, choose_question
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
    if step == 0:
        persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
        english_numbers = '1234567890'
        english_trans = str.maketrans(persian_numbers, english_numbers)
        question_number = matches[0].translate(english_trans)

        if matches[1] == config['username']:
            if has_any_point_for_direct():
                question = "* " + make_guess() + "؟"
            else:
                question = choose_question()
            set_step(plugin, message, 1, {'question_number': question_number, 'question': question, 'self': True})
            current_state['n'] = question_number
            current_state['question'] = question
            current_state['asker'] = config['username']
            return Message(chat_id).set_text(question)
        else:
            set_step(plugin, message, 1, {'question_number': question_number, 'self': False})
            current_state['n'] = question_number

    elif step == 1:
        if get_data_step(message)['self']:

            question = get_data_step(message)['question']
            answer = message['text']
            # This is question You Asked and The answer ...

            current_state['answer'] = message['text']
            history.append(copy.deepcopy(current_state))
            delete_step(message)
            if has_any_point_for_vanahesht():
                vanahesht(make_guess())
            return
        else:
            if message['text'] in ["بله", "خیر"]:
                if int(get_data_step(message)['question_number']) % 20 == 0:
                    set_twenty(True)
            current_state['answer'] = message['text']
            history.append(copy.deepcopy(current_state))
            delete_step(message)


plugin = {
    "name": "question",
    "run": run,
    "patterns": ["([۱۲۳۴۵۶۷۸۹۰]+)\\. @(.+bot)"]
}
