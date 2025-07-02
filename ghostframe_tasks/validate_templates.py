import json
import os
from pathlib import Path
from jsonschema import validate, ValidationError

TEMPLATE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "prompt": {"type": "string"}
    },
    "required": ["title", "prompt"],
}

API_KEY_ENV = "API_KEY"

class InvalidTemplateError(Exception):
    pass

class MissingAPIKeyError(Exception):
    pass


def check_api_key():
    if not os.getenv(API_KEY_ENV):
        raise MissingAPIKeyError(f"Environment variable {API_KEY_ENV} is required")


def validate_template(data: dict) -> None:
    try:
        validate(instance=data, schema=TEMPLATE_SCHEMA)
    except ValidationError as e:
        raise InvalidTemplateError(str(e))


def validate_file(json_path: Path) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    validate_template(data)


def validate_directory(directory: Path) -> None:
    """Validate all JSON templates in *directory* recursively."""
    directory = Path(directory)
    for json_file in directory.rglob('*.json'):
        validate_file(json_file)
