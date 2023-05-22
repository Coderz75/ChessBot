"""
    ChessBot - Play stockfish on discord
    Copyright (C) 2023  Nuaym Syed

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import discord, typing, inspect
from discord.ext import commands

async def setup(bot):
    bot.add_command(_ping)
    bot.add_command(_help)

class buttons(discord.ui.View):
		def __init__(self, oninteraction,timeout=180):
			super().__init__(timeout=timeout)
			global result
			result = oninteraction

		@discord.ui.button(label="MORE",style=discord.ButtonStyle.gray)
		async def blurple_button(self,interaction:discord.Interaction,button):

			await interaction.message.edit(embed= result,view=self)



@commands.hybrid_command(name="ping")
async def _ping(ctx):
    """
    Pong!
    Show's bot's processing speed, as well as delay
    **Usage**
    `{}ping`
    """
    t = await ctx.send('Pong!')
    ms = (t.created_at - ctx.message.created_at).total_seconds() * 1000
    embed = discord.Embed(
        title="Pong",
        description=
        f"Pong, what else? \nOur client delay time was about {round(ctx.bot.latency * 1000)} ms \nMy lag should be about {ms - round(ctx.bot.latency * 1000)} ms\nTotal time taken was {ms}\n"
    )
    embed.set_thumbnail(
        url=
        "https://www.publicdomainpictures.net/pictures/350000/nahled/paddle-bat-ping-pong.png"
    )
    embed.set_footer(
        text=
        f".\nDiscord py version: {discord.__version__}\nResponded in {round(ctx.bot.latency * 1000)} ms"
    )
    embed.set_author(name="Requested by: " + ctx.author.display_name,
                     icon_url=ctx.author.avatar)

    await t.edit(content="", embed=embed)

@commands.hybrid_command(name="help")
async def _help(ctx, args: typing.Optional[str]):
    """
    Shows this message
    **Usage**
    `{}help |module/command|`
    """
    prefix = "chess."
    owner = 754532384984137772

    async def predicate(cmd):
        try:
            return await cmd.can_run(ctx)
        except commands.CommandError:
            return False

    if not args:
        try:
            owner = ctx.guild.get_member(owner).mention
        except:
            pass

        embed = discord.Embed(
            title="Help",
            description=
            f'Use `{prefix}help <module>` to gain more information about that module '
        )
        cogs_desc = ''
        for module in ctx.bot.cogs:
            if str(module) != "Jishaku":
                cogs_desc += f'`{module}` {ctx.bot.cogs[module].__doc__}\n'

        # adding 'list' of cogs to embed
        embed.add_field(name='Modules', value=cogs_desc, inline=False)

        commands_desc = ''
        for command in ctx.bot.walk_commands():
            # if cog not in a cog
            # listing command if cog name is None and command isn't hidden
            if not command.cog_name and not command.hidden:
                x = command.help.split('\n')[0]
                commands_desc += f'`{command.name}` - {x}\n'

        # adding those commands to embed
        if commands_desc:
            embed.add_field(name='Not belonging to a module',
                            value=commands_desc,
                            inline=False)

        embed.add_field(
            name='About',
            value=
            f"{ctx.bot.get_user(ctx.bot.user.id)} is devoloped by <@{owner}>")
    else:

        # iterating trough cogs
        for cog in ctx.bot.cogs:
            # check if cog is the matching one
            if cog.lower() == args.lower():

                # making title - getting description from doc-string below class
                embed = discord.Embed(title=f'{cog} - Commands',
                                      description=ctx.bot.cogs[cog].__doc__,
                                      color=discord.Color.green())

                # getting commands from cog
                for command in ctx.bot.get_cog(cog).get_commands():
                    # if cog is not hidden
                    if not command.hidden:
                        valid = await predicate(command)
                        if valid:
                            embed.add_field(name=f"`{prefix}{command.name}`",
                                            value=command.brief,
                                            inline=False)
                # found cog - breaking loop
                break

        # if args not found
        # yes, for-loops have an else statement, it's called when no 'break' was issued
        else:
            for command in ctx.bot.commands:
                if command.name.lower() == str(args).lower():

                    y = command.name
                    for z in command.aliases:
                        y += "|{}".format(z)

                    a = ""
                    argspec = eval(f"inspect.getfullargspec(_{command.name})")
                
                    reqargs = argspec.args
                    reqargs.remove('self'); reqargs.remove('context')
                    for req in reqargs: a += f" {req}"

                    # making title - getting description from doc-string below class
                    embed = discord.Embed(title=f'{command} - Commands',
                                          description=command.help.format(prefix),
                                          color=discord.Color.green())
                
                    
                    # found cog - breaking loop
                    break

            else:
                embed = discord.Embed(
                    title="Hmmmm",
                    description=
                    f"No module or command found of the instance `{args}`",
                )

    embed.set_footer(
        text=
        f"Discord py version: {discord.__version__}\nResponded in {round(ctx.bot.latency * 1000)} ms"
    )
    embed.set_author(name="Requested by: " + ctx.author.display_name,
                     icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)