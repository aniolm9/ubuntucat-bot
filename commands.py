import urllib.request

def start(bot, chat_id):
    bot.sendMessage(chat_id, "Gràcies per iniciar-me! Soc el bot d'ajuda de l'Ubuntu Catalan Team!")

def ordredia(bot, chat_id):
    fp = urllib.request.urlopen("https://wiki.ubuntu.com/CatalanTeam/Reunions?action=raw")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    pos = mystr.find("(ordreDia)>>")
    inici = mystr.find("|| ", pos)
    final = mystr.find("== Reunions fetes ==", inici)
    sortida = "Ordre del dia:\n" + mystr[inici:final].strip()

    bot.sendMessage(chat_id, sortida)

def avisMati(bot):
    bot.sendMessage(-1980488, "Recordeu que avui a les 22:00 hi ha reunió!")

def avisVespre(bot):
    bot.sendMessage(-1980488, "Recordeu que falta 1 hora per la reunió!")

def avisImmediat(bot):
    bot.sendMessage(-1980488, "Va! Que comença la reunió!")
    ordredia(bot, -1980488)