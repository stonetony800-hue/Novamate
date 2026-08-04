import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Text Messages
WELCOME_TEXT = (
    "สวัสดี {user_name} ยินดีต้อนรับสู่ เว็บ UFANEXT ตรงจาก UFABET! 🎉\n\n"
    "🧧💥 สมัครวันนี้รับเครดิตฟรี 300 บาท หรือฟรีสปิน 300 ครั้ง 💥🧧\n"
    "🎰 คืนเงินเดิมพันทุกวัน!\n"
    "❤️ แจ็คพอตแตกทุกชั่วโมง! 😮 คุณอาจเป็นคนต่อไป 🔥\n\n"
    "🎁 ลุ้นโชคกับรางวัล LUCKY SPIN REWARDS !!\n"
    "💥รับรางวัลเงินสด! 20,545,200 บาท ที่นี่!!💥\n"
    "เราให้โบนัสต้อนรับ 1,500 บาท แก่คุณหากเข้าร่วมวันนี้!!\n\n"
    "🎲 สมัครคลิ๊ก https://ufanext.cc/register/\n"
    "📲 เว็บ UFANEXT https://ufanext.cc"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    user = update.effective_user
    # Get user's first name or fall back to full name / username
    user_name = user.first_name if user.first_name else user.full_name

    # Create inline link buttons for a clean user experience
    keyboard = [
        [
            InlineKeyboardButton("🎲 สมัครสมาชิก (Register)", url="https://ufanext.cc/register/"),
        ],
        [
            InlineKeyboardButton("📲 เข้าสู่เว็บไซต์ (Website)", url="https://ufanext.cc"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Format the dynamic username in the Thai message
    formatted_message = WELCOME_TEXT.format(user_name=user_name)

    await update.message.reply_text(
        text=formatted_message,
        reply_markup=reply_markup,
        disable_web_page_preview=False
    )

def main() -> None:
    """Start the bot."""
    # Retrieves TOKEN from Environment Variables (Set on Render)
    token = os.environ.get("BOT_TOKEN")

    if not token:
        logger.error("No BOT_TOKEN found in environment variables!")
        return

    # Build application
    application = ApplicationBuilder().token(token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))

    # Run the bot (Long Polling)
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
