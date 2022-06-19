from twitchio.ext import commands, sounds
from ddoapi.playerData import playerData
from dotenv import dotenv_values

def prepare(bot):
    bot.add_cog(MyCog())

class MyCog(commands.Cog):
    async def player_done():
        print('Finished playing sound!')

    player = sounds.AudioPlayer(callback=player_done)
    local_config = dotenv_values(".env")

    servers = ["argonnessen", "argo", "cannith", "ghallanda", "khyber", "orien", "sarlona", "thelanis", "wayfinder"]
    for current_server in servers:
        if current_server == "argo":
            real_server = "argonnessen"
        else:
            real_server = current_server

        func = f"\n@commands.command()" \
                "\nasync def {dynamicFunctionName}(self, ctx:commands.Context, *character):" \
                "\n\tif not character:" \
                "\n\t\toutput='To use this command do !server <character name> such as !sarlona temnoc'" \
                "\n\telse:" \
                "\n\t\tddo_playerData = playerData(character[0], '{ddoServer}')" \
                "\n\t\tplayer_data=ddo_playerData.get_character_info()" \
                "\n\t\toutput = self.prettyDdoCharacterInfo(player_data)" \
                "\n\tawait ctx.send(output)\n".format(dynamicFunctionName=current_server, ddoServer=real_server)
        exec(func)

    @commands.command()
    async def botCommands(self, ctx: commands.Context):
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
        await ctx.send(f'I am currently playing this:  ' + self.local_config['CURRENT_BUILD'])

    @commands.command()
    async def builds(self, ctx: commands.Context):
        await ctx.send(f'https://github.com/glassjaws/builds')

    @commands.command()
    async def code(self, ctx: commands.Context):
        await ctx.send(f'The glassbot code can be found at https://github.com/glassjaws/glassbot5000/')

    @commands.command()
    async def latest_video(self, ctx: commands.Context):
        await ctx.send(f'Latest YT video:' + '\n' + self.local_config['VIDEO_TITLE'] + '\n' + self.local_config['VIDEO_URL'])

    @commands.command()
    async def goat(self, ctx: commands.Context):
        sound = sounds.Sound(source="data/sounds/goat.mp3")
        await ctx.send(f'🐐')
        self.player.play(sound)

    @commands.command()
    async def slughead(self, ctx: commands.Context):
        await ctx.send(f'🐌')

    @commands.command()
    async def shame(self, ctx: commands.Context):
        sound = sounds.Sound(source="data/sounds/shame.mp3")
        await ctx.send(f'🔔SHAME 🔔')
        self.player.play(sound)
    
    @commands.command()
    async def maetrim(self, ctx: commands.Context):
        await ctx.send(f'Maetrim is available at:  https://github.com/Maetrim/DDOBuilder')

    @commands.command()
    async def rage(self, ctx: commands.Context):
        sound = sounds.Sound(source="data/sounds/rage.mp3")
        await ctx.send(f'Grog would like to RAAAAAAAAGE!')
        self.player.play(sound)

    @commands.command()
    async def wynnter(self, ctx: commands.Context):
        sound = sounds.Sound(source="data/sounds/wolf.wav")
        await ctx.send(f'	🐺')
        self.player.play(sound)

    @commands.command()
    async def nodens(self, ctx:commands.Context):
        sound = sounds.Sound(source='data/sounds/shortbow.mp3')
        await ctx.send(f'🏹')
        self.player.play(sound)

    def prettyDdoCharacterInfo(self, player_data):
        all_classes=""
        if player_data is None:
            output = f"This character either is not logged in, does not exist on this server, or data is not available yet.  Please note that this data is cached, and may be up to 3 minutes old."
        else:
            for classes in player_data['Classes']:
                if classes['Name'] != None:
                    current_class=(classes['Name'] + ' ' + str(classes['Level']))
                    if all_classes == "":
                        all_classes=current_class
                    else:
                        all_classes = ','.join([all_classes, current_class])
            output = f"{player_data['Name']} is a level {str(player_data['TotalLevel'])} ({all_classes}) {player_data['Race']} {player_data['Gender']}"
        return output

