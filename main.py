from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime



TOKEN: Final = '6840498904:AAFXLs6E9yivLKZsHhLceufR04HhB-1P_N8'
BOT_USERNAME : Final = '@Yumikuro_Alicebot'

async def start_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Master Wena')

async def help_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('What is your command?')

async def custom_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('As you wish!')

def handle_response(text:str) -> str:
    processed: str = text.lower()
    if 'alice' in processed:
        return 'Yes master?'

    if 'str' in processed:
        return 'As You Wish'

    if 'sch' in processed:
        dt = datetime.now()
        date = dt.weekday()
        if date == 0:
            return 'Here are your schedules for today master\n07:30 - 10:00 Konversi Energi Elektrik \n10:15 - 12:45 Mikroprosesor dan Mikrokontroler \n13:30 - 16:00 Pengukuran Besaran Elektrik dan Praktikum'
        elif date == 2:
            return 'Here are your schedules for today master\n07:30 - 10:00 Elektromagnetika \n10:15 - 11:55  Elektronika Daya \n	13:30 - 15:10 Kewirausahaan'
        elif date == 3:
            return 'Here are your schedules for today master\n07:30 - 10:00 Metode Numerik'
        elif date == 4:
            return 'Here are your schedules for today master\n07:30 - 10:00 Pengolahan Sinyal Digital dan Praktikum'

        else:
            return '404 You can rest now'

    return "Sorry but you must be not my master...."

async  def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')


    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return


    else :
            response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)



async def error(update : Update, context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot..')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)


    print('Polling...')
    app.run_polling(poll_interval=3)
