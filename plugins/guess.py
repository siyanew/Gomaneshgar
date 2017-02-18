import asyncio

from message import Message


def make_guess():
    return "سعدی"

@asyncio.coroutine
def run(message, matches, chat_id, step):
    answer = make_guess()
    return Message(chat_id).set_text(answer)


plugin = {
    "name": "guess",
    "run": run,
    "patterns": ["^حدس$"]
}

