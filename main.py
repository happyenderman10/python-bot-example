import os
import asyncio 
import discord
from discord.ext import commands
import random, string
import aiohttp
import requests 
from requests import delete
from random import choice



token = "your-bot-token"
prefix = "your-prefix"
author = "your-name"

client = commands.Bot(command_prefix=prefix)


client.remove_command('help')


@client.event
async def on_ready():
    print("Im ready!")
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="To generate random nitro gift use g!gen",color=0xffb300)
    embed.add_field(name="Gen things", value="``gen``, ``num``")
    embed.add_field(name="Fun", value="``embed``,``dog``,``cat``")
    embed.add_field(name="Request",value="``support``")
    embed.add_field(name="Utility",value="``deletewebhook``,``avatar``,``botinfo``,``hack``,``ping``,``alert``")
    await ctx.send(embed=embed)
@client.command()
async def minecraft(ctx, *,text):
    msg = ctx.message
    await msg.delete()
    msg2 = await ctx.send("opss")
    await msg2.delete()
    await ctx.send(f"https://minecraftskinstealer.com/achievement/20/Achievement+Unlocked%21/{text}")
@client.command()
async def spamchannels(ctx, *,name):
    guild = ctx.message.guild
    n=0
    while(n<=85):
        await guild.create_text_channel(f'{name}') # Decide what should be the name of the text channels that you will create
        n = n+1
@client.command()
async def ping(ctx):
    embed = discord.Embed(title="",description=f" Pong! {round(client.latency * 1000)} ms")
    await ctx.send(embed=embed)
@client.command()
async def gen(ctx):
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    embed = discord.Embed(title="Nitro gen bot",description=" ",color=0x4287f5)
    embed.add_field(name="Generate a random nitro gift", value=f"{code}")
    await ctx.send(embed=embed)
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
            value =  avamember.name
            avatar =  avamember.avatar_url
            embed = discord.Embed(title=f"{value}", color=0xff0026)
            embed.set_image(url=f"{avatar}")
            await ctx.reply(embed=embed)
@client.command()
async def num(ctx):
    code = "" + ('').join(random.choices(string.digits, k=2))
    embed = discord.Embed(title="Generate random numbers",description=f"Here is your random number ``{code}``",color=0x4287f5)
    await ctx.send(embed=embed)
@client.command()
async def embed(ctx, *,content):
    embed = discord.Embed(title="",description=f"{content}",color=0xffb300)
    await ctx.send(embed=embed)
@client.command()
async def support(ctx, *,content):
    user = ctx.message.author
    userm = ctx.message.author.mention
    embed = discord.Embed(title="Support message sent",description="We will see the support message soon!", color=0xffb300)
    embed.add_field(name="Message : ",value=f"```{content}```")
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f"Support message sent By {user}",description="Someone sent a support Request")
    embed.add_field(name="Message : ",value=f"```{content}```")
    channel = client.get_channel(889965822666227773)
    embed = discord.Embed(title='Support request', description='Someone Used the support command', color=0x03b2f8)
    embed.set_author(name=f'{user}')
    embed.add_field(name='Message : ', value=f'```{content}```')
    embed.add_field(name='User mention : ', value=f'{userm}')
    await channel.send(embed=embed)
@client.command()
async def hack(ctx, *,memeber):
     message = await ctx.send(f"Hacking {memeber}")
     await asyncio.sleep(1)
     await message.edit(content="Finding ip adress")
     await asyncio.sleep(1)
     await message.edit(content="Finding last dmed person")
     await asyncio.sleep(1)
     channel = message.channel
     server = ctx.message.guild
     randomMember = random.choice(server.members).mention
     await message.edit(content=f"Last dmed person found! The person is {randomMember}")
     await asyncio.sleep(1)
     await message.edit(content="Email adress and password logged!")
     await asyncio.sleep(1)
     await message.edit(content="Real and danger hack is Done")


@client.command()
async def dog(ctx):
  async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') 
      dogjson = await request.json() 
  embed = discord.Embed(title="Dog!", color=discord.Color.blue()) 
  embed.set_image(url=dogjson['link'])  
  await ctx.send(embed=embed)
@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Bot info : ",description="This is the bot info!", color=0xeb4034)
    embed.add_field(name="Author : ",value=f"{author}")
    embed.add_field(name="Discord.py Version : ",value=f"{discord.__version__}")
    await ctx.send(embed=embed)

@client.command()
async def cat(ctx):
  async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat') 
      dogjson = await request.json() 
  embed = discord.Embed(title="Cat!", color=discord.Color.blue()) 
  embed.set_image(url=dogjson['link'])  
  await ctx.send(embed=embed)
@client.command()
async def deletewebhook(ctx, *,webhook):
   delete(webhook)
   message = ctx.message
   user = ctx.message.author
   await message.delete()
   msg = await ctx.send("Dont try to snipe!")
   await msg.delete()
   embed = discord.Embed(title=":white_check_mark:  Webhook deleted!")
   await ctx.send(embed=embed)
   print(f"{user} deleted a webhook!")
client.run(token)
