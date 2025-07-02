import argparse
import json
from pathlib import Path


def convert_txt_files(input_dir: Path, output_file: Path) -> None:
    entries = []
    for txt_path in input_dir.rglob('*.txt'):
        with txt_path.open('r', encoding='utf-8') as f:
            content = f.read()
        entries.append({'filename': str(txt_path.relative_to(input_dir)), 'text': content})
    with output_file.open('w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description='Convert .txt prompt files to JSON list.')
    parser.add_argument('input_dir', type=Path, help='Directory to search for .txt files')
    parser.add_argument('output', type=Path, help='Path to write JSON output')
    args = parser.parse_args()
    convert_txt_files(args.input_dir, args.output)


if __name__ == '__main__':
    main()
