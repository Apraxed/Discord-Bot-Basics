# **READ ME FIRST!!!**

Discord Bot Basics
=
A beginners guide to [discord.py](https://github.com/Rapptz/discord.py) by [Danny (aka Rapptz)](https://github.com/Rapptz)

The code itself
-
### discord.py has 2 main "Bot Types"

- `bot`
- `client`

No diffrence other than:
- Client `client.run("BOT_TOKEN")` Bot `bot.run("BOT_TOKEN")` 
- Client `@client.command` Bot `@bot.command`
- Client `@client.event` Bot `@bot.event`

This template uses `client` rather then `bot`
=
## STEPS TO GET THE BOT TO RUN

### Make sure to get Python 3.5 or higher
This is required to actually run the bot.

### Install dependencies
This is pip install -U -r requirements.txt

## What everything means

```py
import discord
from discord.ext import commands
import config
import os
``` 
General imports for everything

```py
cfg = config
```
Making it so you can do `cfg.` rather than `config.`

```py
client = commands.Bot(command_prefix = cfg.BOT_PREFIX)
```
Adding the prefix and defining `client`

```py
@client.event
async def on_ready():
    print(client.user.name, 'is online')
    channel =   channel = client.get_channel(cfg.channel_id)
    await channel.send('Bot online')
```
What happens whenever the bot starts

![](/images/yes.png)

```py
@client.command()
async def ping(ctx):
    ping = int(round(client.latency, 3) * 1000)
    await ctx.send(f'{ctx.author.mention} {ping} ms.')
```
`@client.command()` is telling discord that this line is a command

`async def ping(ctx):` `async def` is listing the next part as a definition `ping` is the command (ex: `!ping`) and `(ctx):` is `context` but shortened

`ping = int(round(client.latency, 3) * 1000)` =  the latency (ping) of the bot and defining it as `ping`

`await ctx.send(f'{ctx.author.mention} {ping} ms.')` = `await` is telling the bot to do this next action
`ctx.send` is telling the bot to send this after the prefix and context (in this case, `ping`) (`f'{ctx.author.mention} {ping} ms.')` is telling the bot what to respond with

```py
@client.command()
async def embed(ctx):
    embed = discord.Embed(title = ccfg.Example_Embed_Title, description = ccfg.Example_Embed_Title, color = 0x5865f2) # blurple hex code
    embed.add_field(name = ccfg.Embed_Name_1, value = (ccfg.Embed_Text_1))
    embed.add_field(name = ccfg.Embed_Name_2, value = (ccfg.Embed_Text_2))
    await ctx.send(embed = embed)
```
`embed = discord.Embed` = Defining embed (needed!)

`(title = ccfg.Example_Embed_Title, description = ccfg.Example_Embed_Title, color = 0x5865f2)` = title (configurable in ![commands config](commands_config.py)) and description (configurable in ![commands config](commands_config.py)) and the colors hexadecimal code (hex code), [if you want to find the hex code of your favorite color go here](https://imagecolorpicker.com/color-code/5865f2) `await ctx.send(embed = embed)` sending the embed
