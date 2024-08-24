import logging
import os

from logtail import LogtailHandler
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
LOGTAIL_TOKEN = os.getenv('LOGTAIL_TOKEN')

logger = logging.getLogger(__name__)

def bootstrap():
    # Create Logtail handler
    logtail_handler = LogtailHandler(source_token=LOGTAIL_TOKEN)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logtail_handler, console_handler]
    )
    
    logger.info("Logger initialized")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    return app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /start command")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    app = bootstrap()
    logger.info("Starting bot")
    app.run_polling()