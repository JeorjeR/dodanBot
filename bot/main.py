"""Main file to initialize environment variables and starting application"""
from dotenv import load_dotenv


def main():
    load_dotenv()  # take environment variables from .env
    try:
        from bot.controller import start_bot
        start_bot()
    except (Exception, ) as ex:
        raise ex


if __name__ == "__main__":
    main()
