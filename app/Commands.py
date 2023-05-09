from telegram import Update
from telegram.ext import ContextTypes
from config import *
from Download_Video import Downloader
# import aiohttp


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
    downloader = Downloader(video_url)
    downloader.start()
    downloader.join()
    
    with open("Video.mp4", "wb") as f:
        f.write(downloader.buffer.getvalue())
    title = downloader.get_title()
    await update.message.reply_text(f"Downloading {title}")
    await update.message.reply_text("Whole Fucntion is running coreectly")