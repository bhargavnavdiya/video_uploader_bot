from telegram import Update, Bot
from telegram.ext import ContextTypes
import os
from ByteVideoUploader import *


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!, I can help you to upload video")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This bot is currently in progress. Please contact the admin for any issues")
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")
    
async def m3u8_download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    
    
    await update.message.reply_text("This is m3u8 download command")


async def yt720p_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_url = context.args[0]
    video_bytes = download_video(video_url)
    if video_bytes is not None:
        try:
            await update.message.reply_text("Downloading video...!\nPlease wait...!")
            await context.bot.send_document(chat_id= update.effective_chat.id, document= video_bytes, filename=f"{video_url.split('=')[-1]}.mp4", timeout = 600)
        except Exception as e:
            await update.message.reply_text("Sorry, Something went wrong.\nPlease, Contact admin for more details")
            print(f"Error is {e}")
    
    
    # Send video using telegram.Bot which will not save video to local device
    
    
    # This will save the video then send it to user
    # print(type(stream))
    # with open(stream, 'rb') as video_file:
    #     await update.message.reply_video(stream)
    #     os.remove(stream)