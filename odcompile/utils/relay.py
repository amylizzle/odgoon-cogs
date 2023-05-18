import json
from json import JSONDecodeError

from discord import Embed
from httpx import AsyncClient
from httpx import ConnectTimeout
from httpx import NetworkError
from httpx import ReadTimeout

from odcompile.utils.misc import getEmbed


async def sendCode(listenerurl: str, code: str, timout: int = 900) -> json:
    """
    Communicate with the sandbox server and return the json output
    """
    async with AsyncClient() as client:
        r = await client.post(listenerurl, json={"code_to_compile": code}, timeout=timout)
        return r.json()


async def processCode(self, code: str, full_output: bool = False) -> Embed:
    try:
        r = await sendCode(listenerurl=await self.config.listener_url(), code=code)

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

    return getEmbed(logs=r, full=full_output)
