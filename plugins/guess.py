import asyncio

from bot import history
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):

    answer = 'حافظ'
    return Message(chat_id).set_text("{}".format(answer))


plugin = {
    "name": "guess",
    "run": run,
    "patterns": ["^حدس$"]
}

