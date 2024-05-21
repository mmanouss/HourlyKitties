import discord
from discord.ext import commands, tasks
from botfunctions import envGet, getKitty
from channelIDS import CHANNEL_IDS

BOT_TOKEN = envGet("BOT_TOKEN", False)
CAT_KEY = envGet("CATKEY", False)

bot = commands.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=':3'))
    print(f'Logged in as {bot.user}')
    sendRandomKittyHourly.start()

@bot.slash_command(name="kitty", description="Send a random cat picture!")
async def kitty(ctx):
    url = getKitty(CAT_KEY)
    embed = discord.Embed(title="⁺₊ cat pic for u! ⁺₊", color=0x36393e)
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

@bot.slash_command(name="kitty-help", description="HourlyKitties command information!")
async def help_command(ctx):
    embed = discord.Embed(title="HourlyKitties Commands", color=0x36393e)
    embed.add_field(name="/kitty", value="Send a random cat picture!", inline=False)
    await ctx.respond(embed=embed)
    
@tasks.loop(hours=1)
async def sendRandomKittyHourly():
    await sendRandomKitty()

async def sendRandomKitty():
    for channel_id in CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if channel is None:
            print(f"Channel {channel_id} not found.")
            continue
        
        url = getKitty(CAT_KEY)
        embed = discord.Embed(title="⁺₊ cat pic of the hour! ⁺₊", color=0x36393e)
        embed.set_image(url=url)
        await channel.send(embed=embed)
        print(f"Sent cat to channel {channel_id}.")

bot.run(BOT_TOKEN)