import discord
from discord.ext import commands, tasks
from discord import FFmpegAudio
bot = commands.Bot(command_prefix=".")
@bot.event
async def on_ready():
        bot.change_presence(activity=discord.Game('Vira Radio Testing Station!'))
        print("Logged In")
        bot.remove_command('help')
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
@bot.command(aliases=['paly', 'queue', 'que'])
async def play(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('in da club.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

bot.run('ODkzNTUwMjY5MTQzNTkyOTkx.YVdFiQ.wfheu7odehLwI2NBGmQSz3Q6TKA')
