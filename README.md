# Gomaneshgar
Python Template For Gomaneshgar's Bot Written in Python 3 .

## How to Run ?
First of all install Python >= 3.5 and then install `pip3`.
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
sudo apt-get install python3-pip
```
OR Compile with Source:
```
wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
tar xfz Python-3.5.*
cd Python-3.5.*
./configure --with-ensurepip=install
make
sudo make install
```
Run These commands for Resolving the dependencies.

```
sudo pip3 install pip -U
sudo pip3 install telepot -U
sudo pip3 install demjson
```

## Set Configs & Run
Open config.json then add Group, Token and The bot's Username.After that just run this command to run!
```
python3 bot.py
```

## Description
This bot is plugins based so you can add a lot of plugins in plugins folder. The plugins structure are shown below.

```
import asyncio

from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
     
    return Message(chat_id).set_text("The Championship is started.", parse_mode="Markdown")


plugin = {
    "name": "start",
    "run": run,
    "patterns": ["^آغاز$"]
}
```

This is start plugin and each plugin has some values in a dictionary with plugin name:
```
name --> plugin name 
patterns --> some regex in a list to fire this plugin to run ...
```
Inside run function do everything do you want and then if you want to send message just return this object :
```
return Message(chat_id).set_text("Sample Text")
```
### Vanahesht
If you want to answer, you can use `vanahesht("ANSWER",confident)` function in bot.py.

### Guess
In `plugins/guess.py` there is a function and its name is `make_guess`. Complete this function and it will send the return value when `حدس` message send or after the twenieth question. 

### Send Message Without Firing a Event !!
Your AI can work in other threads (For calculating a new question or sending Vanahesht). If you want Send Message whenever you want just send it into sender_queue :
```
sender_queue.put(Message(config['group']).set_text("TEST")
```

### History
There is a history variable in bot.py that stores all questions with their answer from another bots.

### Please
Please feel free to ask any questions here by issues or on telegram via [@Siyanew](https://t.me/siyanew/)
