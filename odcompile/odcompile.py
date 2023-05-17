from redbot.core import commands
from redbot.core import Config

__version__ = "1.1.0"
__author__ = "Crossedfall"


class ODCompile(commands.Cog):
    """A discord compiler for OpenDream"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 32175847454, force_registration=True)

        default_config = {"listener_url": "http://localhost:5000/compile"}

        self.config.register_global(**default_config)

    @commands.command()
    async def meep(self, ctx):
        """placeholder"""
        await ctx.send("Meep!")
