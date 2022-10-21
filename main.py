"""Main file to initialize environment variables and starting application"""
import os

from dotenv import load_dotenv


def main():
    load_dotenv()  # take environment variables from .env
    try:
        from bot.controller import start_bot
        chat_id = os.environ['CHAT_ID']
        start_bot()
    except (Exception, ) as ex:
        raise ex


if __name__ == "__main__":
    main()
