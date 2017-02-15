import asyncio

from bot import vanahesht
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
    yield from vanahesht("سلام",chat_id)
    return Message(chat_id).set_text("The Championship is started.", parse_mode="Markdown")


plugin = {
    "name": "start",
    "run": run,
    "patterns": ["^آغاز$"]
}

