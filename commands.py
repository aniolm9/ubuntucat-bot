def start(bot, chat_id):
    bot.sendMessage(chat_id, "Gràcies per iniciar-me! Soc el bot d'ajuda a l'Ubuntu Catalan Team!")

def avisMati(bot):
    bot.sendMessage(-1980488, "Recordeu que avui a les 22:00 hi ha reunió!")

def avisVespre(bot):
    bot.sendMessage(-1980488, "Recordeu que falta 1 hora per la reunió!")

def avisImmediat(bot):
    bot.sendMessage(-1980488, "Ja comença la reunió!")