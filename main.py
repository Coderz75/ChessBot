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
import discord, os, traceback
from discord.ext import commands
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = commands.when_mentioned_or('chess.'), intents=intents, description = "Play Chess!", help_command=None, activity = discord.Game(name="chess.help"))


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await setup_hook(client)

async def setup_hook(self):
    await self.load_extension('jishaku')
    await self.load_extension('cogs.config')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    user = await client.fetch_user("754532384984137772")
    embed = discord.Embed(title="ERROR", description= f"```{traceback.format_exception(type(error), error, error.__traceback__)}```",color=0xFF0000)
    print(traceback.format_exception(type(error), error, error.__traceback__))
    await user.send(embed = embed)
    raise error

client.run(os.getenv("TOKEN"))

