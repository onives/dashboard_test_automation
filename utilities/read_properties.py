import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
