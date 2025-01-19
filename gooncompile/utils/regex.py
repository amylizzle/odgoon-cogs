from re import compile

CODE_BLOCK_RE = compile(r"^((`+\S+\\n)|(`{1,3}))(?=\S)|(`{1,3}$)")
COMPILER_ERROR_RE = compile(r"(Compilation failed with (\d*) errors)|([Unknown|Invalid] arg 'DMCompiler\.Argument')")
COMPILER_WARNING_RE = compile(r"Compilation succeeded with (\d*) warnings")
SERVER_ERROR_RE = compile(r"(\[FAIL\]|\[ERRO\])")
SERVER_STARTING_OUTPUT_RE = compile(r"((.|\n)*)\[INFO\] world.log: -------ODC-Start-------")
SERVER_ENDING_OUTPUT_RE = compile(r"\[INFO\] world.log: --------ODC-End--------((.|\n)*)")
INCLUDE_PATTERN = compile(r"#(|\W+)include")
