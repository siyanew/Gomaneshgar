import asyncio

from bot import set_step, delete_step, get_data_step, history
from message import Message

@asyncio.coroutine
def run(message, matches, chat_id, step):
    if step == 0:
        set_step(plugin, message, 1,{'question': matches[2],'username':matches[0]})
        return

    elif step == 1:
        question = get_data_step(message)['question']
        username = get_data_step(message)['username']

        if message['text'] == "بله":
            pass # Do When answer is yes
        if message['text'] == "خیر":
            pass  # Do When answer is no

        # add question and answer to istory list.
        history.append({'username': username + "bot", 'question':question, 'answer':message['text']})

        delete_step(message)
        return Message(chat_id).set_text("سعدی {}".format(message['text']), parse_mode="Markdown")


plugin = {
    "name": "otherquestion",
    "run": run,
    "patterns": ["@(.*)bot :(\\n+)([^\\n]*)"]
}

