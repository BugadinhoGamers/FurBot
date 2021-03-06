# FurBot by BugadinhoGamers (https://github.com/BugadinhoGamers/FurBot)
# Licensed under GPLv3.0

import discord
import random
from datetime import datetime
from datetime import date
from datetime import timezone
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    AnimalList = ["wolf", "dog", "cat", "goat", "eagle", "fox", "lion", "protogen", "cow", "horse"]

    @commands.command()
    async def whichanimal(self, ctx):
        random.seed(ctx.message.author.id * 2)
        await ctx.message.channel.send(self.bot.GetLocale(ctx.message.guild, "fun_youare") + self.AnimalList[random.randint(0,len(self.AnimalList) - 1)])
    
    @commands.command()
    async def pounce(self, ctx, *, pounced):
        embed=discord.Embed(color=0x8000ff)
        embed.set_image(url="https://static1.e926.net/data/06/65/066570f0b541f23c8d03d1956a590167.gif")
        await ctx.message.channel.send(content=ctx.message.author.mention + self.bot.GetLocale(ctx.message.guild, "fun_pounced") + pounced,embed=embed)
    
    @commands.command()
    async def yiff(self, ctx, *, yiffed):
        gif = "https://static1.e926.net/data/07/a9/07a9e5aa8770e86c1b58e117e6deee4a.png"

        embed=discord.Embed(color=0x8000ff)
        embed.set_image(url=gif)
        await ctx.message.channel.send(content=ctx.message.author.mention + self.bot.GetLocale(ctx.message.guild, "fun_yiffed") + yiffed,embed=embed)

    @commands.command()
    async def measuredick(self, ctx):
        random.seed(ctx.message.author.id * 2)

        embed=discord.Embed(title=self.bot.GetLocale(ctx.message.guild, "fun_cocktitle"), description=self.bot.GetLocale(ctx.message.guild, "fun_cockabout") + str(random.randint(0,200) / 10) + "cm", color=0x8000ff)
        await ctx.message.channel.send(embed=embed)
    
    @commands.command()
    async def cumlord(self, ctx):
        if (ctx.message.channel.type is discord.ChannelType.private):
            embed=discord.Embed(title=self.bot.GetLocale(ctx.message.guild, "error1"), description=self.bot.GetLocale(ctx.message.guild, "error3"), color=0xff0000)
            return await ctx.message.channel.send(embed=embed)
    
        random.seed(datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=timezone.utc).timestamp())
        serverUsers = ctx.message.guild.members

        embed=discord.Embed(title=self.bot.GetLocale(ctx.message.guild, "fun_cumtitle"), description=self.bot.GetLocale(ctx.message.guild, "fun_cumis") + serverUsers[random.randint(0,len(serverUsers)-1)].mention, color=0x8000ff)
        await ctx.message.channel.send(embed=embed)
    
    @commands.command()
    async def howmuch(self, ctx, *, stuff):
        bobao = 0
        for letter in stuff:
            bobao += ord(letter)

        random.seed(ctx.message.author.id * int(bobao) * 2)
        bobin = random.randint(0,100)

        embed=discord.Embed(title=self.bot.GetLocale(ctx.message.guild, "fun_howmuch"), description=ctx.message.author.mention + self.bot.GetLocale(ctx.message.guild, "fun_howis") + str(bobin) + "% " + str(stuff), color=0x8000ff)
        await ctx.message.channel.send(embed=embed)

        if (bobin == 100):
            await ctx.invoke(self.bot.get_command('request'), type='sfw', tags=bobao)


def setup(bot):
    bot.add_cog(Fun(bot))

    command = []

    command.append(["\n:bookmark_tabs:", "fun_fun", False])
    command.append(["<:fapgamer:747188878951186433> f-cumlord", "fun_fcumlord", True])
    command.append([":thinking: f-howmuch", "fun_fhowmuch", True])
    command.append([":dog: f-whichanimal", "fun_fwhichanimal", True])
    command.append(["<:subway:744236763735785483> f-yiff", "fun_fyiff", True])
    command.append([":fox: f-pounce", "fun_fpounce", True])

    bot.helpCommand["fun"] = (command)