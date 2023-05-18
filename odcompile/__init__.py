from .odcompile import ODCompile


async def setup(bot):
    await bot.add_cog(ODCompile(bot))
