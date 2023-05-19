import json
from json import JSONDecodeError

from discord import Embed
from httpx import AsyncClient
from httpx import ConnectTimeout
from httpx import NetworkError
from httpx import ReadTimeout

from odcompile.utils.misc import getEmbed


async def sendCode(listenerurl: str, code: str, args: list, timeout: int = 900) -> json:
    """
    Communicate with the sandbox server and return the json output
    """
    async with AsyncClient() as client:
        r = await client.post(listenerurl, json={"code_to_compile": code, "extra_arguments": args}, timeout=timeout)
        return r.json()


async def processCode(self, code: str, args: list, parsed_output: bool = True) -> Embed:
    try:
        r = await sendCode(listenerurl=await self.config.listener_url(), code=code, args=args)

    except (JSONDecodeError, ReadTimeout, AttributeError):
        embed = Embed(
            description="There was a problem with the listener. Unable to retrieve any results!",
            color=0xFF0000,
        )
        return embed
    except (NetworkError, ConnectTimeout):
        embed = Embed(description="Error connecting to listener", color=0xFF0000)
        return embed

    if "build_error" in r.keys():
        embed = Embed(title="Unable to build image", description=f"{r['exception']}", color=0xFF0000)
        return embed
    if "error" in r.keys():
        embed = Embed(title="There was an unrecoverable error", description=r["error"], color=0xFF0000)
        return embed

    return getEmbed(logs=r, parsed_output=parsed_output)
