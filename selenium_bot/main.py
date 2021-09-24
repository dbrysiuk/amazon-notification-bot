from bot import Bot

if __name__ == '__main__':
    # replace URL-Text with product that should be checked on Amazon
    # replase EMAIL-Text where the notification should be sent
    amazon_bot = Bot("URL", "EMAIL")
    amazon_bot.check_product()
