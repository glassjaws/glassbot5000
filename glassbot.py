import os # for importing env vars for the bot to use
from dotenv import load_dotenv
from twitchio.ext import commands, sounds
import ffmpeg

class Bot(commands.Bot):
  def __init__(self):
    # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
    load_dotenv()
    token=os.environ.get('ACCESS_TOKEN')
    prefix=os.environ.get('BOT_PREFIX')
    initial_channels=os.environ.get('CHANNEL')
    super().__init__(token=token, prefix=prefix, initial_channels=[initial_channels])
    self.player = sounds.AudioPlayer(callback=self.player_done)
 
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

  async def player_done(self):
    print('Finished playing sound!')

  @commands.command()
  async def bot_commands(self, ctx: commands.Context):
    await ctx.send(f'Commands can be located here:  https://github.com/glassjaws/glassbot5000/wiki/Commands')
  
  @commands.command()
  async def hello(self, ctx: commands.Context):
    # Send a hello back!
    await ctx.send(f'Hello {ctx.author.name}!')

  @commands.command()
  async def server(self, ctx: commands.Context):
    await ctx.send(f'Heya {ctx.author.name}!  I play on the magnificent Sarlona server.')

  @commands.command()
  async def status(self, ctx: commands.Context):
    await ctx.send(f'I am the glassbot 5000! Exterminate!  Exterminate!')

  @commands.command()
  async def build(self, ctx: commands.Context):
    await ctx.send(f'I am currently playing this:  ' + os.environ.get('CURRENT_BUILD'))

  @commands.command()
  async def builds(self, ctx: commands.Context):
    await ctx.send(f'https://github.com/glassjaws/builds')

  @commands.command()
  async def code(self, ctx: commands.Context):
    await ctx.send(f'The glassbot code can be found at https://github.com/glassjaws/glassbot5000/')

  @commands.command()
  async def latest_video(self, ctx: commands.Context):
    await ctx.send(f'Latest YT video:' + '\n' + os.environ.get('VIDEO_TITLE') + '\n' + os.environ.get('VIDEO_URL'))

  @commands.command()
  async def goat(self, ctx: commands.Context):
    await ctx.send(f'🐐')

  @commands.command()
  async def slughead(self, ctx: commands.Context):
    await ctx.send(f'🐌')

  @commands.command()
  async def shame(self, ctx: commands.Context):
    sound = sounds.Sound(source="data/sounds/shame.mp3")
    await ctx.send(f'🔔SHAME 🔔')
    self.event_player.play(sound)

bot = Bot()
bot.run()
