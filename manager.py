from discord.ext import commands, tasks
from discord.ext.commands import MissingRequiredArgument, CommandNotFound
import discord

class Manager(commands.Cog):


    def init(self, bot):
        self.bot = bot



    @commands.command()
    async def Eae(self, ctx):
        name = ctx.author.name

        response = "Olá, " + name

        await ctx.send(response)

    @commands.command()
    async def say(ctx,mensagem):
     embed = discord.Embed(title=f"{mensagem}", description=f"Mensagem enviada por {ctx.author.name}", color=discord.Color.purple())
     await ctx.send(embed=embed)

    @commands.command()
    async def dm(ctx):
     embed = discord.Embed(title="Não enche!", color=discord.Color.green())

     embed2 = discord.Embed(title="Dm enviada!", color=discord.Color.dark_orange())
     await ctx.send(embed=embed2)
     await ctx.author.send(embed=embed)

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member : discord.Member,reason=None):
     await ctx.send(f"Membro expulso!: {member.mention}\nMotivo: {reason}")
     await member.send(f"Você foi expulso, motivo {reason}")
     await member.kick(reason=reason)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os Argumentos. Digite !help para ver os parâmetros de cada comando")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver todos os comandos")
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
