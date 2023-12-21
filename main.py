import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Command : start getInfo istart_handlernfo")
    
async def initial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Initial Bot.")

def get_token():
    with open('config.json','r') as json_file:
        data = json.load(json_file)
    return data['token']

if __name__ == '__main__':
    token : str = get_token()
    application = ApplicationBuilder().token(token).build()
    
    # initial()
    initial_handler = CommandHandler('initial', initial)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    application.add_handler(initial_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    
    application.run_polling()
