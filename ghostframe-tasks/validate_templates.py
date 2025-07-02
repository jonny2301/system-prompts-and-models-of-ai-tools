import argparse
import json
import re
from pathlib import Path
from typing import List

API_KEY_PATTERN = re.compile(r'(?:sk-\w{10,}|api_key\s*[:=]\s*\S+)', re.IGNORECASE)


def validate_json(path: Path, errors: List[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        errors.append(f"{path}: invalid JSON - {e}")
        return
    if 'prompt' not in data:
        errors.append(f"{path}: missing 'prompt' field")
    if 'tools' in data and not isinstance(data['tools'], list):
        errors.append(f"{path}: 'tools' should be a list")
    if API_KEY_PATTERN.search(json.dumps(data)):
        errors.append(f"{path}: possible API key present; use placeholder")


def validate_text(path: Path, errors: List[str]) -> None:
    text = path.read_text(encoding='utf-8')
    if API_KEY_PATTERN.search(text):
        errors.append(f"{path}: possible API key present; use placeholder")


def main() -> None:
    parser = argparse.ArgumentParser(description='Validate prompt templates.')
    parser.add_argument('directory', type=Path, help='Directory of templates to check')
    args = parser.parse_args()

    errors: List[str] = []
    for file in args.directory.rglob('*'):
        if file.name == 'deploy_checkpoints.json':
            continue
        if file.suffix == '.json':
            validate_json(file, errors)
        elif file.suffix == '.txt':
            validate_text(file, errors)
    if errors:
        print('\n'.join(errors))
        exit(1)
    print('All templates valid.')


if __name__ == '__main__':
    main()
