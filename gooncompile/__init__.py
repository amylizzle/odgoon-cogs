from discord import AppCommandType

from .gooncompile import GoonCompile
from .utils.appCommands import compileMessage


async def setup(bot):
    await bot.add_cog(GoonCompile(bot))
    bot.tree.add_command(compileMessage)


async def teardown(bot):
    bot.tree.remove_command("Compile with OD", type=AppCommandType.message)
