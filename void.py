import discord
import os
from discord.ext import commands
import asyncio 
import random 
import requests
import sys
import threading
import datetime
import json
import aiohttp
from colorama import Fore
import time
from pypresence import Presence

with open('config.json') as f:
    config = json.load(f)

token = config.get('Token')    

void = commands.Bot(command_prefix="?", case_insensitive=True, self_bot=True)
void.remove_command(name='help')

print(f'''
{Fore.LIGHTGREEN_EX}
    ██╗   ██╗  █████╗  ██╗ ██████╗
    ██║   ██║ ██╔══██╗ ██║ ██╔══██╗
    ╚██╗ ██╔╝ ██║  ██║ ██║ ██║  ██║
     ╚████╔╝  ██║  ██║ ██║ ██║  ██║
      ╚██╔╝   ╚█████╔╝ ██║ ██████╔╝
       ╚═╝     ╚════╝  ╚═╝ ╚═════╝  RPC
  
  [>] WELCOME TO VOID RPC
  [>] Discord.gg/hrcxontop
  [>] MADE BY LEGEND
''')
@void.command()
#
#
#
############
#HELP MENU #
############
#
#
#
async def help(ctx, category=None):
    if category is None:
        embed = discord.Embed(color=0x0ce885)
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
        embed.add_field(name='`1.`?amongus', value='This command sets your **AMONG-US** playing status', inline=False)
        embed.add_field(name='`2.`?codmobile', value='This command sets your **Call of Duty** playing status', inline=False)
        embed.add_field(name='`3.`?gtav5', value='This command sets your **GTA V5** playing status', inline=False)
        embed.add_field(name='`4.`?pubg', value='This command sets your **PUBG** playing status', inline=False)
        embed.add_field(name='`5.`?csgo', value='This command sets your **CS-GO** playing status', inline=False)
        embed.add_field(name='`6.`?minecraft', value='This command sets your **MINE-CRAFT** playing status', inline=False)
        embed.add_field(name='`7.`?cyberpunk', value='This command sets your **CYBER PUNK** playing status', inline=False)
        embed.add_field(name='`8.`?farcry', value='This command sets your **FARCRY 5** playing status', inline=False)
        embed.add_field(name='`9.`?fortnite', value='This command sets your **FORTNITE** playing status', inline=False)
        embed.add_field(name='`10.`?custom', value='This command sets your **CUSTOM** playing status', inline=False)
        embed.set_author(name="----> VOID RPC BOT <----")
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
        await ctx.send(embed=embed)

#
#
#        
#######################----MODULES---###############################
#
#
#

@void.command()
#
#
##############
#BGMI MODULE #
##############
#
#
async def codmobile(ctx, *, bgmi="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Call of Duty: Mobile"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **COD-MOBILE**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
################
#GTA V5 MODULE #
################
#
#
async def gtav5(ctx, *, gtav5="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Grand Theft Auto V"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **GTA V5**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
#
##############
#PUBG MODULE #
##############
#
#
#
async def pubg(ctx, *, pubg="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="PlayerUnknown's Battlegrounds"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **PUBG**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
#
##################
#AMONG-US MODULE #
##################
#
#
#
async def amongus(ctx, *, hitman="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Among Us"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **AMONG-US**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
#
##################
#MINECRAFT MODULE #
##################
#
#
#
async def minecraft(ctx, *, hitman="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Minecraft"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **MINE-CRAFT**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
#
###################@
#CYBER-PUNK MODULE #
###################@
#
#
#
async def cyberpunk(ctx, *, hitman="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Cyberpunk 2077"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **CYBER-PUNK**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
@void.command()
#
#
#
###################@
#FORTNITE MODULE #
###################@
#
#
#
async def fortnite(ctx, *, hitman="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Fortnite"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **FORTNITE**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)

@void.command()
#
#
#
###################@
#FORTNITE MODULE #
###################@
#
#
#
async def farcry(ctx, *, hitman="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Far Cry"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **Far Cry**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)

@void.command()
async def info(ctx, category=None):
    if category is None:
        embed = discord.Embed(color=0x0ce885)
        embed.set_author(name="───> INFO MENU <───")
        embed.set_image(url="")
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg")
        embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE BY LEGEND")
        embed.add_field(name='**VOID RPC INFO ->**', value=f'```elm\n> PING -> {round(void.latency * 1000)} ms\n\n> Language -> Python\n\n> Verson -> v1\n\n> Devloper -> Legend \n\n> Tag -> ĦɌCӾ 𒂟†LΣGΣΠD†₊⋆𓆩🥀𓆪†ᵉʳʳᵒʳ⁴⁰⁴#0001```')
        await ctx.send(embed=embed)

@void.command()
#
#
##############
#BGMI MODULE #
##############
#
#
async def csgo(ctx, *, bgmi="HRCX OP", category=None):
  if category is None:
    await void.change_presence(activity=discord.Game(name="Counter-Strike: Global Offensive"))
    embed = discord.Embed(color=0x0ce885)
    embed.add_field(name='VOID RPC', value='----------------------\n\n✅ UPDATED STATUS TO PLAYING : **CS-GO**')
    embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/857496350769545217/867682432841023488/qxNZR3p3_400x400.jpg", text="MADE WITH 💖 BY LEGEND || ?info")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/886121747923992598/886121917461970984/qxNZR3p3_400x400_1.jpg")
    await ctx.send(embed=embed)
#
#
#
#
#    
void.run(token, bot=False)
