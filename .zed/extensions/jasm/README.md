# JASM Zed Extension

Local Zed syntax highlighting and bracket matching for Jaide's `.jasm` files.

Instruction and register vocabulary follows `common/isa.py`, with `SYSCALL` and
`RETURN` recognized ahead of their implementation. Syntax follows
`jasm/language/grammar.py`: directives, macros and `%parameters`, labels,
pointers, nested expressions, and raw strings. Removed instructions are no longer
highlighted as mnemonics. This is syntax support; operand modes and macro expansion
are validated by the assembler.

## Install or reload

Run `zed: install dev extension` in Zed and select this directory:

```text
/Users/josiah/Projects/jaide/.zed/extensions/jasm
```

After an update, rebuild the JASM development extension from Zed's Extensions view.
The manifest references the local grammar repository's `main` branch. Its source
changes must be committed in `grammars/tree-sitter-jasm` before Zed rebuilds it;
Zed clones committed source, not working-tree edits. `grammars/jasm/` and
`grammars/jasm.wasm` are generated build outputs.

## Develop and verify

Use Tree-sitter CLI 0.25.10, as declared by the grammar's `package.json`:

```sh
cd .zed/extensions/jasm/grammars/tree-sitter-jasm
npm install
npx tree-sitter generate --abi 14
cd ../..
TREE_SITTER="$PWD/grammars/tree-sitter-jasm/node_modules/.bin/tree-sitter" python3 verify.py
```

An existing CLI works too: `python3 .zed/extensions/jasm/verify.py`. Set
`TREE_SITTER` to its absolute path if it is not on `PATH`.
Verification checks vocabulary against the canonical ISA, runs syntax regression
cases, parses every kernel source file, and compiles/runs both Zed queries.
