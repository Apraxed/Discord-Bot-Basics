import discord
from discord.ext import commands
import config, commands_config
import os

ccfg = commands_config
cfg = config

client = commands.Bot(command_prefix = cfg.BOT_PREFIX)

@client.event
async def on_ready():
    print(client.user.name, 'is online')
    channel =   channel = client.get_channel(cfg.channel_id)
    await channel.send('Bot online')

# Test command
@client.command()
async def test(ctx):
    await ctx.send('Test success')

# Ping command
@client.command()
async def ping(ctx):
    ping = int(round(client.latency, 3) * 1000)
    await ctx.send(f'{ctx.author.mention} {ping} ms.')

@client.command()
async def embed(ctx):
    embed = discord.Embed(title = ccfg.Example_Embed_Title, description = ccfg.Example_Embed_Title, color = 0x5865f2) # blurple hex code
    embed.add_field(name = ccfg.Embed_Name_1, value = (ccfg.Embed_Text_1))
    embed.add_field(name = ccfg.Embed_Name_2, value = (ccfg.Embed_Text_2))
    await ctx.send(embed = embed)

# Makes the bot run
client.run(os.environ['TOKEN'])
