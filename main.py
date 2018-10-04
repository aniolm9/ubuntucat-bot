#!/usr/bin/env python3
# Developed by Xaldiks

import time
import telepot
import functions
import commands
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s from chat_id: %d' % (command, chat_id))

    if (command == "/start" or command == "/start@UbuntuCat_bot"):
        commands.start(bot, chat_id)
    elif (command == "/ordredia" or command == "/ordredia@UbuntuCat_bot"):
        commands.ordredia(bot, chat_id)

f = open("TOKEN", "r")
TOKEN = f.readline().rstrip()
f.close()
bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    functions.avisos(bot)
    time.sleep(0.8)
