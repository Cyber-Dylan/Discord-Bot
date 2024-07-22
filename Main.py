import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')  # Set command prefix to be '!'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:  # Ignore messages from the bot itself
        return

    if ctx.content.startswith('!ping'):  # Check if message starts with
'!ping'
        await ctx.send('Hello')  # Reply with 'Hello'

bot.run('YOUR_BOT_TOKEN')
