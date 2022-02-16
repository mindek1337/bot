import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions
import random






client = commands.Bot(command_prefix= ".")

    







client.remove_command("help")









@client.event
async def on_ready():
    print("online")






@client.command()
async def help(ctx):
    embed=discord.Embed(title="HELP", description="Prefix = .", color=0x00c20d)
    embed.add_field(name="undefined", value="undefined", inline=True)
    embed.set_footer(text="EZBOT")
    await ctx.send(embed=embed)













@client.command()
async def status(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Zbanowano {member} za {reason} ", delete_after=10)

@client.command()
async def iq(ctx):
    numer = random.randrange(0, 200)
    await ctx.channel.send(numer)

@client.command()
async def banana(ctx):
    numer = random.randrange(1, 20)
    await ctx.channel.send(numer)

@client.command()
async def uwu(ctx):
    await ctx.send("UwU")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("nie podałeś argumentu")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('🚫')


@client.command()
async def clear(ctx, ilosc = 50):
    await ctx.channel.purge(limit = ilosc)

@client.command()
async def author(ctx):    
    embed=discord.Embed(title="AUTHORS", color=0x1acb38)
    embed.add_field(name="PYTHON DEV", value="mindek#3836", inline=False)
    embed.add_field(name="BOT CEO", value="mindek#3836", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def version(ctx):
    embed=discord.Embed(title="VERSION", color=0x16a71f)
    embed.add_field(name="CLIENT VERSION", value="v0.1", inline=False)
    await ctx.send(embed=embed)







client.run("OTQyNzM1MjEyNjQxNjczMjI2.Ygo0lQ.HKRVTdRyrc9KHc4CgYjCwIRDMt8")
