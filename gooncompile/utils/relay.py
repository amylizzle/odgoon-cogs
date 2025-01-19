import json
from json import JSONDecodeError

from discord import Embed
from httpx import AsyncClient
from httpx import ConnectTimeout
from httpx import HTTPStatusError
from httpx import NetworkError
from httpx import ReadTimeout
from packaging.version import parse as parse_version

from gooncompile._exceptions import BadVersion
from gooncompile.utils.logger import log
from gooncompile.utils.misc import getEmbed


async def sendCode(listenerurl: str, code: str, args: list, build_config: str, timeout: int = 900) -> json:
    """
    Communicate with the sandbox server and return the json output
    """
    async with AsyncClient() as client:
        r = await client.post(
            url=f"{listenerurl}/compile",
            json={"code_to_compile": code, "extra_arguments": args, "build_config": build_config},
            timeout=timeout,
        )
        return r.json()


async def processCode(self, code: str, args: list, build_config: str, parsed_output: bool = True) -> Embed:
    listener_url = await self.config.listener_url()
    try:
        listener_version = await getVersion(listenerurl=listener_url)
        checkCompatibility(listener_version)
        r = await sendCode(listenerurl=listener_url, code=code, args=args, build_config=build_config)

    except (JSONDecodeError, ReadTimeout, AttributeError) as e:
        embed = Embed(
            description="There was a problem with the listener. Unable to retrieve any results!",
            color=0xFF0000,
        )
        log.error(e)
        return embed
    except (NetworkError, ConnectTimeout) as e:
        embed = Embed(description="Error connecting to listener", color=0xFF0000)
        log.error(e)
        return embed
    except BadVersion as e:
        embed = Embed(title="Compiler server out of date", description=e, color=0xFF0000)
        return embed

    if "build_error" in r.keys():
        embed = Embed(title="Unable to build image", description=f"{r['exception']}", color=0xFF0000)
        return embed
    if "error" in r.keys():
        embed = Embed(title="There was an unrecoverable error", description=r["error"], color=0xFF0000)
        return embed

    return getEmbed(logs=r, parsed_output=parsed_output)


def checkCompatibility(version: str) -> bool:
    if parse_version(version=version) < parse_version("0.3.1"):
        raise BadVersion(f"Version {version} does not support build configs and needs to be updated.")


async def getVersion(listenerurl: str) -> str:
    try:
        async with AsyncClient() as client:
            r = await client.get(url=f"{listenerurl}/version")
            r.raise_for_status()
            return r.json()["version"]
    except HTTPStatusError as e:
        if "404 NOT FOUND" in str(e):
            raise BadVersion("The compiler server is too old and needs to be updated! Unable to fetch version number.")
        else:
            raise
