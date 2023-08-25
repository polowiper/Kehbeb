import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import urllib
import os
import json
intents = discord.Intents.all()
bote = discord.Client(intents=intents)
tree = app_commands.CommandTree(bote)


@tree.command(name = "randomkehbeb", description="envoie une image de kehbeb aléatoire")
async def randomkehbeb(interaction):
    fchoice = random.choice(os.listdir('kehbeb/'))
    fchoice = f"{os.getcwd()}/kehbeb/{fchoice}"
    file = discord.File(f"{fchoice}", filename="kehbeb.jpg")
    await interaction.response.send_message(file=file)

@tree.command(name = "kehbebinfo", description="donne des infos sur un kehbeb en particulier")
async def kehbebinfo(interaction, kehbebe: int = 0):
    droprate = round((1/len(os.listdir(r"kehbeb\\"))), 4)
    with open('kehbebs.json') as e: 
        kehbebs = json.load(e)
        message = list(kehbebs.keys())
    polo = bote.get_user(823143840813809666)
    if kehbebe == 0:
        embed = discord.Embed(title="Tou lé kehbeb mgl", colour=discord.Colour.random())
        embed.set_author(name = "Polo", url="https://github.com/polowiper", icon_url=(polo.avatar.url))
        for i in message:
            embed.add_field(name=i, value=(f"Numéro : {kehbebs[i]['id']}"))
        await interaction.response.send_message(embed=embed)
    if kehbebe > len(os.listdir('kehbeb/')):
        await interaction.response.send_message("Mgl lui il éxist pa")
    else:
        embed = discord.Embed(title=message[kehbebe-1], colour=discord.Colour.random(), 
        description=(f"""{kehbebs[message[kehbebe-1]]['info']}
Chef : {kehbebs[message[kehbebe-1]]['chef']}
Adresse : {kehbebs[message[kehbebe-1]]['location']}
Rareté : {round((droprate * 100), 2)}%

Kebeb N°{kehbebs[message[kehbebe-1]]['id']}

        """))
        file = discord.File(f"kehbeb\\kehbeb{kehbebe}.jpg", filename="kehbeb.jpg")
        embed.set_image(url=f"attachment://kehbeb.jpg")
        embed.set_author(name= "Polo", url="https://github.com/polowiper", icon_url=(polo.avatar.url))
        await interaction.response.send_message(file=file, embed=embed)
    

@bote.event
async def on_ready():
    await tree.sync()
@bote.event
async def on_message(msg):
    num = 0
    decimal = False
    decinum = 1
    undecinum = 1
    bruh = []
    if '€' in msg.content:
        for aya in msg.content:
            if aya.isdigit():
                if decimal == False:
                    if aya == 0:
                        num = float(num + str(aya))
                        undecinum = 10
                    else: 
                        num = float(num) * (undecinum) 
                        num = float(num + float(aya))
                        undecinum = 10 
                if decimal == True:
                    if aya == 0:
                        num = float(num + str(aya))
                        decinum *= 10
                    else:
                        aya = float(aya) / (10 * decinum)
                        num = float(num + float(aya))
                        decinum *= 10
            if "," in str(aya):
                decimal = True
            if aya == "€":
                bruh.append(num)
                decinum = 1
                undecinum = 1
                decimal = False
                num = 0
                pass
        po = 0
        for i in bruh:
            bruh[po] = round((i / 7.86), 5)
            po += 1
        if len(bruh) <= 1:
            if bruh[0] < 1:
                await msg.channel.send("wallah c " + str(bruh[0]) + " kehbebs chef t trop pauvre la honte")
            elif bruh[0] > 5 and bruh[0] < 10:
                await msg.channel.send("wallah c " + str(bruh[0]) + " kehbebs chef tu khalass tes potes ou quoi?")
            elif bruh[0] > 10:
                await msg.channel.send("wallah c " + str(bruh[0]) + " kehbebs chef t Elon Musk wsh")
            else:
                await msg.channel.send("wallah c " + str(bruh[0]) + " kehbebs chef")    
        if len(bruh) > 1:
            bo = "wallah c "
            b = 0
            for i in bruh:
                if b == (len(bruh) - 2):
                    bo += str(bruh[b]) + " et "
                else:
                    bo += str(bruh[b]) + ", "
                b += 1
            bo += " kehbeb chef pfiouuuu sa fé beaucoup"
            await msg.channel.send(bo)

bote.run("")