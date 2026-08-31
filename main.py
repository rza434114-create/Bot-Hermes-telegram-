#!/usr/bin/env python3
"""
Bot Hermes Telegram - Main Bot Script
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get configuration
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
HERMES_API_KEY = os.getenv('HERMES_API_KEY')

if not BOT_TOKEN:
    logger.error("❌ TELEGRAM_BOT_TOKEN not found in .env file")
    exit(1)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command handler"""
    await update.message.reply_text(
        "👋 سلام! من ربات Hermes هستم.\n"
        "برای کمک، /help را بنویسید."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help command handler"""
    help_text = """
    📚 دستورات موجود:
    
    /start - شروع کار
    /help - این پیام راهنما
    /info - اطلاعات ربات
    
    💬 هر پیامی بفرستید و من پاسخ خواهم داد!
    """
    await update.message.reply_text(help_text)


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Info command handler"""
    info_text = """
    🤖 Bot Hermes Telegram v1.0
    
    🚀 قابلیت‌ها:
    • پاسخ‌های هوشمند
    • پردازش متن طبیعی
    • کمک و راهنمایی
    
    📧 توسعه‌دهنده: rza434114-create
    🔗 منبع: https://github.com/NousResearch/hermes-agent
    """
    await update.message.reply_text(info_text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages"""
    user_message = update.message.text
    user_name = update.effective_user.first_name
    
    logger.info(f"📨 پیام از {user_name}: {user_message}")
    
    # TODO: Integrate with Hermes Agent
    response = f"🤖 سلام {user_name}!\n\nپیام شما دریافت شد: {user_message}\n\n(جواب هوشمند به زودی اضافه می‌شود)"
    
    await update.message.reply_text(response)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error"""
    logger.error(f"❌ Exception while handling an update: {context.error}")


def main() -> None:
    """Start the bot"""
    print("🚀 Bot Hermes Telegram شروع می‌شود...")
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the Bot
    print("✅ ربات فعال است. Ctrl+C برای توقف...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
