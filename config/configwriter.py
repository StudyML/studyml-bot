from configparser import ConfigParser

config = ConfigParser()
config.add_section('main')
config.set('main', 'port', '1000')
config.set('main', 'mainpage', '/your-webpage.html')
config.set('main', 'apikey', 'YOUR-API-KEY')

with open('..\\config2.ini', 'w') as f:
    config.write(f)