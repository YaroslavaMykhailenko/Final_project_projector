from config import bot
from handlers.menu import main_menu
from handlers.donation import donation_process


def start():
    main_menu()
    donation_process()

start()

bot.polling(none_stop=True)
