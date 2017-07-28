import urllib.request

class BotCommander:
    _apikey = None

    def __init__(self, apikey):
        self._apikey = apikey

    def isCommand(self, requestedMessage):
        if (isinstance(requestedMessage, str) != True):
            requestedMessage = str(requestedMessage)

        return (requestedMessage.startswith('/', 0, 1))

    def parseCommand(self, sender, requestedMessage):
        if (isinstance(requestedMessage, str) != True):
            requestedMessage = str(requestedMessage)

        if (self.isCommand(requestedMessage)):
            args = requestedMessage.split(' ', 1) # split only once
            args[0] = args[0][1:]
            args[0] = str.replace(args[0], '@studymlbot', '') # remove unnecessary bot's name in command

            args[0] = args[0].lower()
            args[1] = args[1].lower()

            return args
        else:
            return None

    def processCommand(self, sender, requestedMessage):
        if (isinstance(requestedMessage, str) != True):
            requestedMessage = str(requestedMessage)

        # Process only if the message begins with "/" (command)
        msgReturn = None

        if (self.isCommand(requestedMessage) != True):
            return None

        args = self.parseCommand(sender, requestedMessage)

        if (args != None):
            if (args[0] == '말해'):
                msgReturn = self.getSayItCommand(sender, args)

        return msgReturn

    def getSayItCommand(self, sender, args):
        self.sendMessage(sender, args[1])
        return True

    def sendMessage(self, receiverID, message):
        #https: // api.telegram.org / bot426541811: AAHvsEkn5rEiFgwQic7s6 - CCxGP9fDtJQ - U / sendMessage?chat_id = 205357200 & text = % 22Hello! % 22
        #urllib.quote(u"Müller".encode('utf8'))
        urllib.request.urlopen('https://api.telegram.org/bot' +  self._apikey + '/sendMessage?chat_id=' + receiverID + '&text=' + urllib.request.quote(message.encode('utf8')))
