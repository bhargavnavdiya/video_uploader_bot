from Constants import *
from telegram import Update
from telegram.ext import ContextTypes

# Function to decide response string
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if processed in ["hello", "hi", "hello!", "hi!"]:
        return "Hey there!, How can I serve you today?"
    
    if processed in ["how are you?", "whatsapp!", "whatsapp", "how is it going?"]:
        return "I am good, How about you?"
    
    return 'Something goes wrong!, Please provide valid command'

# Function responsibel to send a response string
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    #handles response if bot is used in group chat
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    #handles response if bot is used privately by user
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)
    
# Function to handle Error messages    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')