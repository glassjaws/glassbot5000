import os
from wsgiref.simple_server import WSGIRequestHandler # for importing env vars for the bot to use
from dotenv import dotenv_values
from twitchio.ext import commands, sounds
import json
from ddoapi.playerData import playerData

class Bot(commands.Bot):
  def __init__(self):
    # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
    token=local_config['ACCESS_TOKEN']
    prefix=local_config['BOT_PREFIX']
    initial_channels=local_config['CHANNEL']

    super().__init__(token=token, prefix=prefix, initial_channels=[initial_channels])

    self.media_player=False

  async def event_ready(self):
    # We are logged in and ready to chat and use commands...
    print(f'Logged in as | {self.nick}')
    print(f'User id is | {self.user_id}')

  async def event_message(self, message):
    # Messages with echo set to True are messages sent by the bot...
    # For now we just want to ignore them...
    if message.echo:
      return

    # Print the contents of our message to console...
    print(message.content)

    # Since we have commands and are overriding the default `event_message`
    # We must let the bot know we want to handle and invoke our commands...
    await self.handle_commands(message)
    
  @commands.command()
  async def reload_bot(self, ctx: commands.Context):
    if ctx.author.name == 'glass_jaws':
      print(f'{ctx.author.name} is reloading the bot_commands module')
      bot.reload_module('bot_commands')
      await ctx.send(f'Bot Commands module reloaded')
    else:
      await ctx.send(f'You do not have permission to run this command {ctx.author.name}')

local_config = dotenv_values(".env")
bot = Bot()
bot.load_module('bot_commands')
bot.run()
