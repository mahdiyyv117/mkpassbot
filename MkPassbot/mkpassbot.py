from telegram import *
from telegram.ext import *
import string
import random

tokena = ""
upder = Updater(tokena, use_context=True)
desp = upder.dispatcher


def main():
    desp.add_handler(CommandHandler("start", start))
    desp.add_handler(CommandHandler("mknewpass", mknewpass))
    upder.start_polling()


def start(update, context):
    update.message.reply_text("Welcome to Password Maker bot")


def mknewpass(update, context):
    update.message.reply_text("Number of characters \nplease enter an integer")
    desp.add_handler(MessageHandler(Filters.text, mkpass))


def mkpass(update, context):
    try:
        numch = int(update.message.text)
        character = string.ascii_letters + string.digits + string.punctuation
        password = ""
        if numch < 8:
            update.message.reply_text("please enter a larger number")
        else:
            for i in range(numch):
                password += random.choice(character)
            update.message.reply_text(f"your password:\
            \n{password} \nuse /mknewpass for the create new password")
    except ValueError:
        update.message.reply_text("please enter the correct value\
        \ntry again with the /mknewpass command")


print("server started")
main()
