#!/bin/bash

# Bot Hermes Telegram - Installation Script
# This script installs Hermes Agent and dependencies

set -e

echo "🚀 Bot Hermes Telegram - نصب و راه‌اندازی شروع..."
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 نصب نیست. لطفاً ابتدا Python 3 را نصب کنید"
    exit 1
fi

echo "✅ Python 3 پیدا شد: $(python3 --version)"

# Create virtual environment
echo ""
echo "📦 ایجاد محیط مجازی..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "📤 آپدیت pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 نصب وابستگی‌ها..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠️  requirements.txt پیدا نشد"
fi

# Install Hermes Agent
echo ""
echo "🤖 نصب Hermes Agent..."
pip install hermes-agent

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo ""
    echo "📝 ایجاد فایل .env..."
    cp .env.example .env 2>/dev/null || cat > .env << 'EOF'
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

# Hermes Configuration
HERMES_API_KEY=your_api_key_here
HERMES_MODEL=hermes-2-pro-mistral-7b

# Database
DATABASE_URL=sqlite:///./hermes.db
EOF
    echo "✅ فایل .env ایجاد شد. لطفاً آن را تکمیل کنید"
fi

echo ""
echo "=================================================="
echo "✅ نصب تکمیل شد!"
echo ""
echo "📋 مراحل بعدی:"
echo "1. فایل .env را تکمیل کنید با اطلاعات خود"
echo "2. دستور زیر را برای فعال‌سازی محیط مجازی اجرا کنید:"
echo "   source venv/bin/activate"
echo "3. برای شروع bot:"
echo "   python main.py"
echo ""
echo "🌐 برای کمک بیشتر: https://github.com/NousResearch/hermes-agent"
