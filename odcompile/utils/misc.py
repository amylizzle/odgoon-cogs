import json

from discord import Embed
from redbot.core.utils.chat_formatting import box
from redbot.core.utils.chat_formatting import escape

from odcompile.utils.regex import CODE_BLOCK_RE
from odcompile.utils.regex import COMPILER_ERROR_RE
from odcompile.utils.regex import COMPILER_WARNING_RE
from odcompile.utils.regex import SERVER_ENDING_OUTPUT_RE
from odcompile.utils.regex import SERVER_ERROR_RE
from odcompile.utils.regex import SERVER_STARTING_OUTPUT_RE


def cleanupCode(content: str) -> str | None:
    """
    clears those pesky codeblocks
    """
    content = escape(content)
    if content.startswith("`") and content.endswith("`"):
        content = CODE_BLOCK_RE.sub("", content)[1:]
        return content.strip("\n")
    elif content.endswith("`"):
        content = CODE_BLOCK_RE.sub("", content)
        return content.strip("\n")

    return None


def splitArgs(args: str, delimiter: str = "`") -> dict:
    """
    Take a list of arguments and split them based on the delimiter.

    Returns a dict of arguments
    """
    args_dict = {}

    args = args.split(sep=delimiter, maxsplit=1)
    args_dict["code"] = args[1]
    args_dict["args"] = [arg.replace("\n", "") for arg in args[0].split(" ")]
    args_dict["parsed"] = True

    if "--no-parsing" in args_dict["args"]:
        args_dict["parsed"] = False
        args_dict["args"].remove("--no-parsing")

    return args_dict


def getEmbed(logs: json, parsed_output: bool = True) -> Embed:
    """
    Generates a discord embed based on the provided logs
    """
    if "build_error" in logs.keys():
        embed = Embed(title="Unable to build image", description=f"{logs['exception']}", color=0xFF0000)
        return embed

    compile_log = (logs["compiler"][:1200] + "...") if len(logs["compiler"]) > 1200 else logs["compiler"]

    run_log = parseRunOutput(logs["server"], parsed_output=parsed_output)
    run_log = (run_log[:1200] + "...") if len(run_log) > 1200 else run_log

    compiler_output = box(escape(compile_log, mass_mentions=True, formatting=True))
    execution_output = box(escape(run_log, mass_mentions=True, formatting=True))

    if logs["timeout"]:
        embed = Embed(
            title="Execution timed out (30 seconds)",
            description=f"Compiler Output:\n{compiler_output}\nExecution Output:\n{execution_output}",
            color=0xD3D3D3,
        )
        return embed
    if COMPILER_ERROR_RE.search(compile_log) is not None:
        embed = Embed(
            title="Errors found during compilation!",
            description=f"Compiler Output:\n{compiler_output}",
            color=0xFF0000,
        )
        return embed

    if int(COMPILER_WARNING_RE.search(compile_log).group(1)) > 0:
        embed = Embed(
            title="Warnings found during compilation!",
            description=f"Compiler Output:\n{compiler_output}\nExecution Output:\n{execution_output}",
            color=0xFFCC00,
        )
    elif SERVER_ERROR_RE.search(run_log) is not None:
        embed = Embed(
            title="Errors found during execution!",
            description=f"Compiler Output:\n{compiler_output}\nExecution Output:\n{execution_output}",
            color=0xFF0000,
        )
    else:
        embed = Embed(
            description=f"Compiler Output:\n{compiler_output}\nExecution Output:\n{execution_output}", color=0x00FF00
        )
    return embed


def parseRunOutput(logs: str, parsed_output: bool) -> str:
    """
    Parse the run output to make it a lot more readable
    """
    if parsed_output is True:
        logs = SERVER_STARTING_OUTPUT_RE.sub("", logs)
        logs = SERVER_ENDING_OUTPUT_RE.sub("", logs)
    return logs
