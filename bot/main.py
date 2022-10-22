"""Main file to initialize environment variables and starting application"""
import os

from dotenv import load_dotenv


def main():
    load_dotenv()  # take environment variables from .env
    try:
        from bot.web.controller import start_bot
        start_bot()
    except (Exception, ) as ex:
        raise ex


if __name__ == "__main__":
    main()

# TODO сделать класс логирования когда появится возщможность добавлять фотки
# TODO чтобы логировать не только текст но и изображения и аудио
# TODO сдеать возможность добавлять фото и текст написав боту какую-то команду а затем отправим содержимое
# TODO добавить аудиосообщения
