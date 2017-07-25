from flask import Flask
from flask import request
import json
import urllib.request
import urllib.parse
from configparser import ConfigParser

# read configuration
config = ConfigParser()
config.read('config.ini')

app = Flask(__name__)

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
    msgtext = result['message']['text']

    print(chatid + " " + msgtext)

    # read api key from external config (for security)
    print("https://api.telegram.org/bot" + config["main"]["apikey"] + "/sendMessage?chat_id=" + chatid + "&text=" + urllib.parse.quote(msgtext, encoding="utf-8"))
    urllib.request.urlopen("https://api.telegram.org/bot" + config["main"]["apikey"] + "/sendMessage?chat_id=" + chatid + "&text=" + urllib.parse.quote(msgtext, encoding="utf-8"))

    #print(content)
    #print(content.message.text)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config["main"]["port"])