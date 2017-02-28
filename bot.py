from os.path import dirname, realpath, join
from queue import Queue
import demjson
import re
import asyncio
import telepot
import telepot.aio
from os import walk

from aifunctions import init
from message import Message

WD = dirname(realpath(__file__))
plugins = []
config = {}
user_steps = {}
sender_queue = Queue()
current_state = {"n": 0, "asker": "", "question": "", "answer": ""}
is_run = False

history = []  # This is a List that stores question in an dictionary contains 3 fields : 1. username 2. question 3. answer


def get_config():
    global config
    file = open(join(WD, "config.json"), "r")
    config = demjson.decode(file.read())
    file.close()


def save_config():
    file = open(join(WD, "config.json"), "w")
    file.write(demjson.encode(config))
    file.close()


def load_plugins():
    global plugins
    get_config()
    plugins = []

    for (dirpath, dirnames, filenames) in walk("plugins"):
        for pluginName in filenames:
            plugin_dir = join(WD, "plugins", pluginName)
            values = {"name": pluginName}
            with open(plugin_dir, encoding='utf-8') as f:
                code = compile(f.read(), plugin_dir, 'exec')
                exec(code, values)
                f.close()
            plugin = values['plugin']
            plugins.append(plugin)


def make_usersteps(message):
    return message['chat']['id']


def set_step(plugin, message, step, data={}):
    user_steps[make_usersteps(message)] = {"name": plugin['name'], 'step': step, 'data': data}


def delete_step(message):
    id = make_usersteps(message)
    if id in user_steps:
        del user_steps[id]


def get_data_step(message):
    return user_steps[make_usersteps(message)]['data']


def set_run(s):
    global is_run
    is_run = s


@asyncio.coroutine
def vanahesht(answer):
    yield from sender(Message(config['group']).set_text(">>> {}".format(answer)))


@asyncio.coroutine
def handle_messages(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    user_step = make_usersteps(message)
    if message['text'] == "آغاز":
        set_run(True)
    if message['text'] == "پایان":
        set_run(False)
    if is_run:
        if chat_id == config['group']:
            if message['text'] in ["خیر", "نمی‌دانم", "بله", "نمیدانم", "نمی دانم"]:
                if user_step in user_steps:
                    for plugin in plugins:
                        if plugin['name'] == user_steps[user_step]['name']:
                            return_value = yield from  plugin['run'](message, [""], chat_id,
                                                                     user_steps[user_step]['step'])
                            if return_value:
                                yield from sender(return_value)
                            break
            elif 'text' in message:
                for plugin in plugins:
                    for pattern in plugin['patterns']:
                        if re.search(pattern, message['text'], re.IGNORECASE | re.MULTILINE):
                            matches = re.findall(pattern, message['text'], re.IGNORECASE)
                            return_value = yield from plugin['run'](message, matches[0], chat_id, 0)
                            if return_value:
                                yield from sender(return_value)

                                # Ordinal Treat


@asyncio.coroutine
def sender(message):
    yield from  bot.sendMessage(message.chat_id, message.text, parse_mode=message.parse_mode,
                                disable_web_page_preview=message.disable_web_page_preview,
                                disable_notification=message.disable_notification,
                                reply_to_message_id=message.reply_to_message_id,
                                reply_markup=message.reply_markup)


@asyncio.coroutine
def check_queue():
    while 1:
        while not sender_queue.empty():
            yield from sender(sender_queue.get())
        yield from asyncio.sleep(0.1)



init(current_state,history)
load_plugins()
bot = telepot.aio.Bot(config['token'])
answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop({'chat': handle_messages,
                                   'edited_chat': handle_messages}))
loop.create_task(check_queue())
print(config.get("username") + ' Started ...')

loop.run_forever()
