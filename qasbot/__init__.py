
from telegram.ext import (Updater, ConversationHandler, CommandHandler,
                          MessageHandler, Filters)
from .commands import info_umum, info_khusus, tanya_jawab, selesai, mulai, CHOOSING, TYPING_REPLY, TYPING_CHOICE
from .logging import logger


def run(TOKEN):
    """
    Menjalankan Bot
    """
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', mulai)],
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(Sejarah|Alamat|Fasilitas)$'),
                                      info_umum),
                       MessageHandler(Filters.regex('^Tanya lain...$'),
                                      info_khusus)
                       ],

            TYPING_CHOICE: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Selesai$')),
                               tanya_jawab)],

            TYPING_REPLY: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Selesai$')),
                               selesai)],
        },

        fallbacks=[MessageHandler(Filters.regex('^Selesai$'), selesai)]
    )

    dp.add_handler(conv_handler)

    logger.info('bot dimulai...')
    updater.start_polling()
    updater.idle()