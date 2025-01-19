<h1 align="center">OpenDream/Goonstation Cogs</h1>

## Overview
A collection of RedBot cogs for running code against the Goonstation codebase with the OpenDream project

Forked from https://github.com/OpenDreamProject/od-cogs and *lightly* modified.

| Cog        | Description                                                                                                                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OD Compile | **Compiles and runs DM code using OpenDream**.<br><br>`gooncompileset` - OD Compiler Settings<br>`gooncompile` - Sends code to a compilation environment and returns the results*<br><br>Requires: httpx<br><br>* Requires additional setup, check below for more information |

## Setup

### RedBot:

Setup for your RedBot V3 instance is a straightforward process. Ensure that your bot runs on python 3.11 and follow the below steps to add the repo and install the cog(s).

1. Add this repo with `[p]repo add odgoon-cogs https://github.com/amylizzle/odgoon-cogs`
2. Install the cog(s) you want to use, `[p]cog install odgoon-cogs gooncompile`
3. Load the newly installed cog(s) with `[p]load gooncompile`

To use gooncompile's context commands, you'll also need to register the interactions with discord. To do so,

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
	- ![image](https://github.com/user-attachments/assets/18dfaa83-d6d3-4d08-8a92-16ed20d28085)
- **Using Goonstation code**
  	- ![image](https://github.com/user-attachments/assets/831f8003-b32f-44f8-a84f-01a67d82dc24)
- **Using the Unit Test framework**
	- ![image](https://github.com/user-attachments/assets/a06ec131-b267-4bcf-95af-d2857dcb4dfc)
- **Standard compilerbot stuff**
	- ![image](https://github.com/user-attachments/assets/7b262866-7e0f-4c57-bf71-937230397504)
 	
 
 


</details>

### Contact:

For questions/concerns, feel free to submit a new issue.
