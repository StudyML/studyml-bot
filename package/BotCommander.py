class BotCommander:
    def __init__(self):
        pass

    def isCommand(self, requestedMessage):
        return (str.startswith(requestedMessage, 0, 1) == '/')

    def parseCommand(self, requestedMessage):
        if (self.isCommand(requestedMessage)):
            args = requestedMessage.split(' ', 1) # split only once
            args[0] = args[0][1:]
            args[0] = str.replace(args[0], '@studymlbot', '') # remove unnecessary bot's name in command

            return args.lower()
        else:
            return None

    def processCommand(self, requestedMessage):
        # Process only if the message begins with "/" (command)
        msgReturn = None

        if (self.isCommand(requestedMessage) is not True):
            return None

        args = self.parseCommand(requestedMessage)

        if (args[0] == '/말해'):
            msgReturn = self.getSayItCommand(args)

        return msgReturn

    def getSayItCommand(self, args):
        return args[1]