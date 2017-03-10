import asyncio
import copy

from aifunctions import make_guess
from bot import current_state, history, delete_step, set_step
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
    if step ==0:
        current_state['question'] = matches[1].strip()
        set_step(plugin, message, 1)

    if step == 1:
        if message['text'] in ["بله", "خیر"]:
            if current_state['n'] % 20 == 0:
                return Message(chat_id).set_text(make_guess())

        current_state['answer'] = message['text']
        history.append(copy.deepcopy(current_state))
        delete_step(message)


plugin = {
    "name": "otherquestion",
    "run": run,
    "patterns": ["(.+):\n(.*)"]
}
