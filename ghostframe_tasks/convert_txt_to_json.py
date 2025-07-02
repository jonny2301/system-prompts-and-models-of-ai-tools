import json
from pathlib import Path

def txt_to_json(txt_path: Path, json_path: Path | None = None) -> Path:
    txt_path = Path(txt_path)
    if json_path is None:
        json_path = txt_path.with_suffix('.json')
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    if not lines:
        data = {"title": "", "prompt": ""}
    else:
        data = {"title": lines[0], "prompt": "\n".join(lines[1:])}
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    return json_path

def convert_directory(directory: Path) -> list[Path]:
    directory = Path(directory)
    json_files = []
    for txt_file in directory.glob('*.txt'):
        json_files.append(txt_to_json(txt_file))
    return json_files
