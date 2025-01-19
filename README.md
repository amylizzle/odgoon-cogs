<h1 align="center">OpenDream/Goonstation Cogs</h1>

## Overview
A collection of RedBot cogs for running code against the Goonstation codebase with the OpenDream project

Forked from https://github.com/OpenDreamProject/od-cogs and *lightly* modified.

| Cog        | Description                                                                                                                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OD Compile | **Compiles and runs DM code using OpenDream**.<br><br>`odcompileset` - OD Compiler Settings<br>`odcompile` - Sends code to a compilation environment and returns the results*<br><br>Requires: httpx<br><br>* Requires additional setup, check below for more information |

## Setup

### RedBot:

Setup for your RedBot V3 instance is a straightforward process. Ensure that your bot runs on python 3.11 and follow the below steps to add the repo and install the cog(s).

1. Add this repo with `[p]repo add od-cogs https://github.com/amylizzle/odgoon-cogs`
2. Install the cog(s) you want to use, `[p]cog install odgoon-cogs odcompile`
3. Load the newly installed cog(s) with `[p]load gooncompile`

To use odcompile's context commands, you'll also need to register the interactions with discord. To do so,

1. Enable the commands with `[p]slash enablecog gooncompile`
2. Sync the interactions with `[p]slash sync` (Note: This can take up to 1-hour for Discord to fully sync the commands)

_Replace [p] with your bot's prefix_

---

### GoonCompile

The GoonCompile cog parses provided DM code and sends it to an external environment which will compile, run, and generate an output to be returned in Discord.

In order to use this cog, you will need to either use a preestablished environment or host your own using this listener: https://github.com/amylizzle/od-compiler-bot/tree/goon_compile

Short one-liners can be provided in basic code-markdown, for example:
`world.log << "Hello, World!"`

Multi-line or explicit code must be contained within a codeblock, for example:
```dm
world.log << 'Hello,'
world.log << "World!"
```
If you're using multiple functions, or if your code requires indentation, you must define a `/proc/main()` as shown below.
```dm
/proc/example()
	world.log << "I'm an example function!"

/proc/main()
	example()
```
#### Arguments

You can pass extra command line arguments to the compiler by adding them before the codeblock.

Adding `--no-parsing` before the codeblock will provide the full execution output instead of a parsed version.

_Code will always be compiled with the latest version of OpenDream_

<details>
	<summary>Example screenshots</summary>

- **Quick compile**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/5b558831-4e12-42dd-89da-fa014a0dfa1a)
- **Compiling with multiple procs**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/4e6bbda6-db84-4978-b0b0-2fc983a1af31)
- **Compiler warnings**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/28a7ea06-4740-4813-a125-8bb422b8a594)
- **Compiler errors**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/00179f34-4a08-42d1-93dc-8c6c592b30d1)
- **Passing arguments to the compiler**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/378dd849-afa7-4024-8983-b9f44e8c6881)
- **Passing multiple arguments at once and disabling the parsed output**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/d13c003c-86e6-4bac-951d-00d42a4ac746)
- **Using the context menu to compile**
	- ![context_compile](https://github.com/OpenDreamProject/od-cogs/assets/26130695/f33fbabb-cec6-4c8b-9e24-8ff71b2553bd)

</details>

### Contact:

For questions/concerns, feel free to submit a new issue.
