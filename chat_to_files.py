import re


def parse_chat(chat):# -> List[Tuple[str, str]]:
    # Get all ``` blocks
    regex = re.compile(r"`([^`]+?)`:\n```.+?\n(.+?)```", re.DOTALL)
    matches = regex.finditer(chat)

    return [(match.group(1), match.group(2)) for match in matches]


def to_files(chat, workspace):
    workspace['all_output.txt'] = chat

    files = parse_chat(chat)
    for file_name, file_content in files:
        workspace[file_name] = file_content
