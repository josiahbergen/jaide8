"""Check ISA vocabulary, parser regressions, and Zed queries. Run from anywhere."""
import ast
import os
from pathlib import Path
import re
import subprocess

EXTENSION = Path(__file__).resolve().parent
ROOT = EXTENSION.parents[2]
GRAMMAR = EXTENSION / "grammars/tree-sitter-jasm"
CLI = os.environ.get("TREE_SITTER", "tree-sitter")


def enum_names(name):
    module = ast.parse((ROOT / "common/isa.py").read_text())
    enum = next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == name)
    return {node.targets[0].id for node in enum.body if isinstance(node, ast.Assign)}


def vocabulary(rule):
    source = (GRAMMAR / "grammar.js").read_text()
    return set(re.search(rf"{rule}:.*?\(\?i:([^)]*)\)", source)[1].split("|"))


def run(*args):
    subprocess.run([CLI, *map(str, args)], cwd=GRAMMAR, check=True)


assert vocabulary("mnemonic") == enum_names("INSTRUCTIONS") | {"SYSCALL", "RETURN"}
assert vocabulary("register") == enum_names("REGISTERS")
run("test")
files = sorted((ROOT / "kernel").rglob("*.jasm"))
run("parse", "--quiet", *files)
for query in ("highlights.scm", "brackets.scm"):
    run("query", "--quiet", EXTENSION / "languages/jasm" / query, *files)
print(f"ISA vocabulary, corpus, {len(files)} kernel files, and both Zed queries passed.")
