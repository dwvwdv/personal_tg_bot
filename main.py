import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import yfinance as yf
import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_token():
    with open('config.json','r') as json_file:
        data = json.load(json_file)
    return data['token']

def getTicker(code : str,startDate : str,endDate : str):

    df = yf.Ticker(code).history(period="max",start=startDate,end=endDate)
    return df


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Command : start getInfo istart_handlernfo")
    
async def initial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Initial Bot.")

async def yfget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = "0050.TW"
    startDate = f'{time.strftime("%Y", time.localtime())}-01-01'
    endDate = time.strftime("%Y-%m-%d", time.localtime()) # get now time

    df = getTicker(code,startDate,endDate)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=df.to_string())

if __name__ == '__main__':
    token : str = get_token()
    application = ApplicationBuilder().token(token).build()
    
    # initial()
    initial_handler = CommandHandler('initial', initial)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    yfget_handler = CommandHandler('yfget', yfget)
    application.add_handler(initial_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(yfget_handler)
    
    application.run_polling()
