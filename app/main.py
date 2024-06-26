import sys
#importing path because config module is in different folder
sys.path.insert(0, 'C:\\Users\\bharg\\Downloads\\BUbot')

from config import *
from Responses import *
from Commands import *
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

if __name__ =='__main__':
    print("Starting bot...")
    app = Application.builder().token(API_KEY).build()
    
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('m3u8', m3u8_download_command))
    app.add_handler(CommandHandler('yt720p', yt720p_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    
    # Errors
    app.add_error_handler(error)
    
    # Response check timing
    print('Polling')
    app.run_polling(poll_interval = 3)