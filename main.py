#!/usr/bin/env python3
# Developed by Xaldiks

import time
import datetime
import telepot
import commands
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if (command == "/start"):
        commands.start(bot, chat_id)

f = open("TOKEN", "r")
TOKEN = f.readline().rstrip()
f.close()
bot = telepot.Bot(TOKEN)



MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:

    # Timing alarms
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    weekday = now.weekday()
    day = now.day
    print(hour, minute, second, weekday, day)

    if (hour == 10 and minute == 0 and second == 5 and weekday == 2 and day < 8):
        commands.avisMati(bot)
    elif (hour == 21 and minute == 0 and second == 5 and weekday == 2 and day < 8):
        commands.avisVespre(bot)
    elif (hour == 22 and minute == 0 and second == 30 and weekday == 2 and day < 8):
        commands.avisImmediat(bot)


    time.sleep(0.8)
