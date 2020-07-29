import os

import discord
from discord.ext import commands

PRESENCE: str = "booping everybody :D"
PREFIX: str = ">"
TOKEN: str = "" # DONT MAKE THIS PUBLIC, KEEP IT A SECRET


@commands.command()
async def beep(ctx):
    await ctx.send("Boop!")


    #THE HELL IS THIS LENNY
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        """Initialise the Bot class.

        Arguments:
            commands {Bot} -- The discord.commands Bot class.
        """
        super().__init__(*args, **kwargs)
        super().__init__(command_prefix=PREFIX,case_insensitive=True)
        self.remove_command("help")
        self.add_command(beep)

    async def on_ready(self):
        """Run on bot ready."""
        print(f"Logged in as {self.user} with id {self.user.id}.")

        game = discord.Game(PRESENCE)
        await self.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        """Run on every recieved message.

        Arguments:
            message {discord.Message} -- The message that was recieved.
        """
        # Ignore Bot
        if message.author.bot:
            return

    
        # Process Commands
        await self.process_commands(message)

    
    
if __name__ == "__main__":
    bot = Bot(command_prefix=PREFIX)
    bot.run(TOKEN, bot=True, reconnect=True)

   