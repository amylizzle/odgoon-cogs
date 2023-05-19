import re

from redbot.core import checks
from redbot.core import commands
from redbot.core.config import Config

from odcompile.utils.misc import cleanup_code
from odcompile.utils.misc import splitArgs
from odcompile.utils.relay import processCode

__version__ = "1.1.0"
__author__ = "Crossedfall"

INCLUDE_PATTERN = re.compile(r"#(|\W+)include")


class ODCompile(commands.Cog):
    """A discord compiler for OpenDream"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 32175847454, force_registration=True)

        default_config = {"listener_url": "http://localhost:5000/compile"}

        self.config.register_global(**default_config)

    @commands.group()
    @checks.admin_or_permissions(administrator=True)
    async def odcompileset(self, ctx):
        """
        DM Compiler settings
        """
        pass

    @odcompileset.command()
    async def listener(self, ctx, url: str = None):
        """
        Set the full URL for the listener

        Should be similar to: http://localhost:5000/compile
        """

        try:
            await self.config.listener_url.set(url)
            await ctx.send(f"Listener URL set to: {url}")
        except (ValueError, KeyError, AttributeError):
            await ctx.send("There was an error setting the listener's URL. Please check your entry and try again.")

    @commands.command()
    async def odcompile(self, ctx, *, input: str):
        """
        Compile and run DM code

        This command will attempt to compile and execute given DM code. It will respond with the full compile log along with any outputs given during runtime. If there are any errors during compilation, the bot will respond with a list provided by OpenDream.

        The code must be contained within a codeblock, for example:
        ```
        world.log << 'Hello world!'
        ```
        If you're using multiple functions, or if your code requires indentation, you must define a `proc/main()` as shown below.
        ```
        proc/example()
            world.log << "I'm an example function!"

        proc/main()
            example()
        ```
        You can pass extra command line arguments to the compiler by adding them before the codeblock.

        Adding `--no-parsing` before the codeblock will provide the full execution output instead of a parsed version.

        __Code will always be compiled with the latest version of OpenDream__
        """
        cleaned_input = splitArgs(args=input)

        code = cleanup_code(cleaned_input["code"])
        if code is None:
            return await ctx.send("Your code has to be in a code block!")
        if INCLUDE_PATTERN.search(code) is not None:
            return await ctx.send("You can't have any `#include` statements in your code.")

        message = await ctx.send("Compiling. If there have been any updates, this could take a moment....")

        async with ctx.typing():
            embed = await processCode(
                self=self, code=code, args=cleaned_input["args"], parsed_output=cleaned_input["parsed"]
            )
            await ctx.send(embed=embed)
            return await message.delete()
