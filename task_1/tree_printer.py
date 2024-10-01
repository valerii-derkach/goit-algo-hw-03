from pathlib import Path

# ANSI-коди для виводу
RESET = '\033[0m'
BOLD = '\033[01m'
CYAN = '\033[96m'
YELLOW = '\033[93m'

def colored(text, color_code):
    return f"{color_code}{text}{RESET}"

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    # рекурсивно виводимо структуру директорії у вигляді дерева
    if path.is_dir():
        print(indent + prefix + colored(f"{path.name}/", BOLD + YELLOW))

        indent += "    " if prefix else ""
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            pointer = "└── " if is_last else "├── "
            display_tree(child, indent, pointer)
    else:
        print(indent + prefix + colored(path.name, CYAN))
