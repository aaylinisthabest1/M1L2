import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx):
    roll_result = random.randint(1, 6)
    await ctx.send(f"Your dice rolled a {roll_result}!")

@bot.command()
async def start(ctx):
    print('Bot is online!')

@bot.command()
async def joke(ctx):
    шутки = [
        "Почему учёные не доверяют атомам? Потому что они составляют всё!",
        "Я сказал моей жене, что она рисует брови слишком высоко. Она выглядела удивленной.",
        "Почему пугало получило награду? Потому что оно было выдающимся в своей области!",
        "Я читаю книгу о антигравитации. Её невозможно отложить!",
        "Как называется фальшивая спагетти? Импаста!"
    ]
    await ctx.send(random.choice(шутки))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
        
bot.run("SECRET CODE")
