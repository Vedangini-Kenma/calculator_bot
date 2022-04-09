import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

my_secret = os.environ['key']

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print('ready')

@bot.command()
async def add(ctx, num1, num2):
  await ctx.reply(float(num1)+float(num2))

@bot.command()
async def sub(ctx, num1, num2):
  await ctx.reply(float(num1)-float(num2))

@bot.command()
async def mul(ctx, num1, num2):
  await ctx.reply(float(num1)*float(num2))

@bot.command()
async def div(ctx, num1, num2):
  await ctx.reply(float(num1)/float(num2))

keep_alive() 
bot.run(my_secret)