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

def setup(bot):
    bot.add_command(_stockfish)

@commands.hybrid_command(name="stockfish")
async def _stockfish(ctx):
    Bp,Bn,Bb,Br,Bq,Bk,    Wk,Wq,Wr,Wb,Wn,Wp ="♙""♘""♗""♖""♕""♔""♚""♛""♜""♝""♞""♟"
    s = " "

    grid = [
        Br,Bn,Bb,Bq,Bk,Bb,Bn,Br,
        Bp,Bp,Bp,Bp,Bp,Bp,Bp,Bp,
        s ,s ,s ,s ,s ,s ,s ,s ,
        s ,s ,s ,s ,s ,s ,s ,s ,
        s ,s ,s ,s ,s ,s ,s ,s ,
        s ,s ,s ,s ,s ,s ,s ,s ,
        Wr,Wn,Wb,Wq,Wk,Wb,Wn,Wr,
        Wp,Wp,Wp,Wp,Wp,Wp,Wp,Wp,
    ]
    out = ""
    for i in range(len(grid)):
        out += grid[i]
        if i % 8 == 0:
            out += "\n"

    await ctx.send(out)