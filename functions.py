import commands
import datetime

def avisos(bot):
    # Timing alarms
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    weekday = now.weekday()
    day = now.day
    #print(hour, minute, second, weekday, day)

    if (hour == 10 and minute == 0 and second == 5 and weekday == 2 and day < 8):
        commands.avisMati(bot)
    elif (hour == 20 and minute == 0 and second == 5 and weekday == 2 and day < 8):
        commands.avisVespre(bot)
    elif (hour == 20 and minute == 55 and second == 5 and weekday == 2 and day < 8):
        commands.avisImmediat(bot)
