from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    @botcmd                               # this tag this method as a command
    def hello(self, mess, args):          # it will respond to !hello
        """ this command says hello """   # this will be the answer of !help hello
        return 'Hello World !'            # the bot will answer that
