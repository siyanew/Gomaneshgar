import asyncio

from bot import config, set_step, delete_step, get_data_step
from message import Message

@asyncio.coroutine
def run(message, matches, chat_id, step):
    if step == 0:
        question_number = matches
        question = "سوال شماره {}\n آیا سعدی است؟".format(question_number)
        set_step(plugin, message, 1, {'question':question})
        # This is a sample message that send when you return it.
        return Message(chat_id).set_text(question)

    elif step == 1:
        question = get_data_step(message)['question']
        answer = message['text']
        # This is question You Asked and The answer ...

        delete_step(message)
        return Message(chat_id).set_text("سعدی {}".format(message['text']), parse_mode="Markdown")


plugin = {
    "name": "question",
    "run": run,
    "patterns": ["([۱۲۳۴۵۶۷۸۹۰]+). @"+config['username']]
}
