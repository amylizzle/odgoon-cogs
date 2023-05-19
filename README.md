<h1 align="center">OpenDream Cogs</h1>

## Overview
A collection of RedBot cogs for the OpenDream project

| Cog        | Description                                                                                                                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OD Compile | **Compiles and runs DM code using OpenDream**.<br><br>`odcompileset` - OD Compiler Settings<br>`odcompile` - Sends code to a compilation environment and returns the results*<br><br>Requires: httpx<br><br>* Requires additional setup, check below for more information |

## Setup

### RedBot:

Setup for your RedBot V3 instance is a straightforward process.

1. Add this repo with `[p]repo add od-cogs <url>`
2. Install the cog(s) you want to use, `[p]cog install od-cogs odcompile`
3. Load the newly installed cog(s) with `[p]load odcompile`

_Replace [p] with your bot's prefix_

---

### ODCompile

The ODCompile cog parses provided DM code and sends it to an external environment which will compile, run, and generate an output to be returned in Discord.

In order to use this cog, you will need to either use a preestablished environment or host your own using this listener: https://github.com/OpenDreamProject/od-compiler-bot

Short one-liners can be provided in basic code-markdown, for example:
`world.log < "Hello, World!"`

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
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/4191b2dc-dc4b-41d4-908d-b8a558b811fa)
- **Compiling with multiple procs**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/4d20e22c-bd5a-42f8-90ea-b53d386531fa)
- **Compiler warnings**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/ee8ba2ec-cbf5-46cd-ab00-e4be14242412)
- **Compiler errors**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/6cf0fde0-5547-4ddc-b7d9-76fdb5ccabf6)
- **Passing arguments to the compiler**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/4c5d510f-f03a-4dc6-a785-487da62841ca)
- **Passing multiple arguments at once and disabling the parsed output**
	- ![image](https://github.com/OpenDreamProject/od-cogs/assets/26130695/3e0ac942-2be3-49a0-9714-61700754a7d3)
</details>

### Contact:

For questions/concerns, feel free to submit a new issue.
