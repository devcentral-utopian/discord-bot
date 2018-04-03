# Import all commands
from commands.test import Test

class CommandHandler:
    """CommandHandler is used to call the correct command and handle help"""

    # Command Prefix and Client are passed on by bot.py so that the commands can send messages
    def __init__(self, prefix, client):
    
        # Used to keep track of all commands available
        self.commandlist = [
            Test()
        ]
        self.prefix = prefix
        self.client = client

    async def handle(self, message):
    """ Calls the command specified in message.content"""
        for command in self.commandlist:
            if self.is_alias(command, message.content):
                await command.execute(self.client, message, message.content.split(" ")[1:]):


    def is_alias(self, cmd, message):
    """ Check if message.content is an alias of cmd"""
        for alias in cmd.aliases:
            if message.lower().startswith(self.prefix + alias.lower()):
                return True
        return False
