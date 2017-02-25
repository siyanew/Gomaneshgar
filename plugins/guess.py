import asyncio

from aifunctions import make_guess
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
    answer = make_guess()
    return Message(chat_id).set_text(answer)


plugin = {
    "name": "guess",
    "run": run,
    "patterns": ["^حدس$"]
}

