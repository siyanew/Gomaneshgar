import asyncio

from bot import current_state


@asyncio.coroutine
def run(message, matches, chat_id, step):
    if step == 0:
        current_state['asker'] = matches[0]
        current_state['question'] = matches[1]
        return


plugin = {
    "name": "otherquestion",
    "run": run,
    "patterns": ["(.+):\n(.*؟)"]
}
