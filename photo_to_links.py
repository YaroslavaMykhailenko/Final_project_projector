import requests
from config import bot
import constants as const
from handlers.donation import temporary_table

token_imgbb = '145648c2d3ed72ff27e02bc39b23e1b8'


@bot.message_handler(content_types="photo")
def save_photo_from_messaage(message):
    url_to_download = bot.get_file_url(message.photo[-1].file_id)
    temporary_table.update({
        'photo_link_download': url_to_download,
        'photo_link_view': upload_photo_link(url_to_download),
    })

    msg = bot.send_message(message.chat.id, const.PROCESS_GET_PHOTO_MSSG)
    bot.send_message(message.chat.id, const.SUCCESS_ADD_PHOTO_MSSG)


def upload_photo_link(link_photo):
    unload_link = requests.get(
        f'https://api.imgbb.com/1/upload?expiration=600&key={token_imgbb}&image={link_photo}'
    )
    # посилання на фото на ресурсі
    view_photo_link = unload_link.json()['data']['url']
    return view_photo_link


if __name__ == '__main__':
    bot.infinity_polling()
