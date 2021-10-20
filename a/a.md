Config.js Example 
```json
{
    "token": "bot-token",
    "prefix": "prefix"
}
```
Bot example 
```py
import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("ready")
@client.command()
async def test(ctx):
    await ctx.send("Hi!")

client.run("token")
```
