from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import re

# Token Bot Anda
TOKEN = 'TOKEN_BOT'
# Nama file untuk menyimpan data
FILE_NAME = 'data.txt'

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    # Pesan yang dikirim ketika pengguna mengetik /start
    message = (
        'Kirimkan gua URL dengan format "https://t.me/dogshouse_bot/join?startapp=reference" gua extrak\n\n'
        'Karyawannya @Jerry1Billion\n'
        'Donate: 0x6Fc6Ea113f38b7c90FF735A9e70AE24674E75D54'
    )
    update.message.reply_text(message)

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    # Pola regex untuk menemukan teks setelah '=' dalam URL
    match = re.search(r'[\?&]startapp=([^&]+)', text)
    if match:
        reference = match.group(1)
        output = f"{user_id}|{reference}"
        # Menyimpan output ke file
        with open(FILE_NAME, 'a') as file:
            file.write(output + '\n')
        response_message = f"Tersimpan: {output}"
        update.message.reply_text(response_message)
    else:
        update.message.reply_text('Kirim URL nu bener anjing, contoh "https://t.me/dogshouse_bot/join?startapp=referensi_anda".')

def main() -> None:
    # Membuat Updater dan mendapatkan bot
    updater = Updater(TOKEN, use_context=True)

    # Mendapatkan dispatcher untuk mendaftarkan handler
    dp = updater.dispatcher

    # Mendaftarkan handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Mulai bot
    updater.start_polling()

    # Menunggu hingga bot dihentikan
    updater.idle()

if __name__ == '__main__':
    main()
