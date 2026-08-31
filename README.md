# 🤖 Bot Hermes Telegram

یک ربات تلگرام هوشمند با قابلیت‌های Hermes Agent

## ✨ ویژگی‌ها

- 🚀 پاسخ‌های هوشمند و سریع
- 🔒 امن و محافظ‌شده
- ⚙️ قابل تنظیم
- 📊 پشتیبانی از پایگاه داده

## 📋 پیش‌نیازها

- Python 3.8 یا بالاتر
- pip (مدیر بسته Python)
- یک توکن ربات Telegram

## 🚀 نصب سریع

### گزینه 1: استفاده از اسکریپت نصب

```bash
chmod +x install.sh
./install.sh
```

### گزینه 2: نصب دستی

```bash
# ایجاد محیط مجازی
python3 -m venv venv
source venv/bin/activate  # روی Windows: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# نصب Hermes Agent
pip install hermes-agent
```

## ⚙️ تنظیم

1. فایل `.env` را از `.env.example` کپی کنید:
```bash
cp .env.example .env
```

2. اطلاعات خود را در `.env` وارد کنید:
```
TELEGRAM_BOT_TOKEN=your_token
HERMES_API_KEY=your_api_key
```

## 🏃 اجرا

```bash
# فعال‌سازی محیط مجازی
source venv/bin/activate

# شروع ربات
python main.py
```

## 📚 منابع

- [Hermes Agent Documentation](https://github.com/NousResearch/hermes-agent)
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📝 لایسنس

MIT License

## 💬 پشتیبانی

برای مشکلات و پرسش‌ها، Issues را باز کنید.

---

**ساخته شده با ❤️ و Hermes Agent**
