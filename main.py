import discord
from discord.ext import commands
import config
import os

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
# pingme command
@client.command()
async def pingme(ctx):
    await ctx.send(f'{ctx.author.mention} get pinged <:h_:840397056194772993>')

# Help cmd
client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'help', description = f'Made by <@{cfg.ownerid}>', color = discord.Color.blurple())
    embed.add_field(name = 'Commands:', value=(f'{cfg.BOT_PREFIX)}test,{cfg.BOT_PREFIX)}ping, {cfg.BOT_PREFIX)}pingme(just in case you want to)')
    embed.add_field(name = 'Prefix', value = (cfg.BOT_PREFIX))
    await ctx.send(embed = embed)

# Makes the bot run
client.run(os.environ['TOKEN'])