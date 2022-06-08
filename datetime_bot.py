from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from datetime import datetime
from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот, показывающий время. Напишите мне что-нибудь, и ты узнаешь время!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Только показываю время...")


def time(update, context):
    update.message.reply_text(str(datetime.now().time()).split('.')[0])


def date(update, context):
    update.message.reply_text(str(datetime.now().date()))


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("date", date))

    text_handler_tm = MessageHandler(Filters.text, time)
    text_handler_dt = MessageHandler(Filters.text, date)

    dp.add_handler(text_handler_tm)
    dp.add_handler(text_handler_dt)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
