from configparser import ConfigParser
from flask import Flask
from flask import request
from package.BotCommander import BotCommander
import json
import urllib.parse
import os

# change working directory to current path (pycharm issue)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# read configuration
config = ConfigParser()
config.read('config.ini')

app = Flask(__name__)

bot = BotCommander(config["main"]["apikey"])

@app.route("/")
def main():
    return "Hello"

@app.route(config["main"]["mainpage"], methods=["GET", "POST"])
def hello():
    #print(request.data)

    result = json.loads(request.data.decode("utf-8"))
    print(result)

    #{"update_id":823873437,"message":{"message_id":21,"from":{"id":205552210,"first_name":"FirstName","last_name":"LastName","language_code":"ko-KR"},"chat":{"id":205552210,"first_name":"FirstName","last_name":"LastName","type":"private"},"date":1500854858,"text":"ASDF"}}
    #print(result)

    chatid = str(result['message']['chat']['id'])

    if ('message' in result):
        if ('text' in result['message']):
            msgtext = result['message']['text']

    print(chatid + " " + msgtext)

    # read api key from external config (for security)
    print("https://api.telegram.org/bot" + config["main"]["apikey"] + "/sendMessage?chat_id=" + chatid + "&text=" + urllib.parse.quote(msgtext, encoding="utf-8"))

    bot.processCommand(chatid, msgtext)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config["main"]["port"])