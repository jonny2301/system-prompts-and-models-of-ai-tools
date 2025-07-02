import os
import json
import pytest
from ghostframe_tasks import validate_templates


def test_validate_template_success(tmp_path):
    data = {"title": "t", "prompt": "p"}
    json_file = tmp_path / "tpl.json"
    json_file.write_text(json.dumps(data))
    os.environ[validate_templates.API_KEY_ENV] = "dummy"
    validate_templates.validate_file(json_file)


def test_validate_template_failure(tmp_path):
    data = {"title": "t"}
    json_file = tmp_path / "tpl.json"
    json_file.write_text(json.dumps(data))
    os.environ[validate_templates.API_KEY_ENV] = "dummy"
    with pytest.raises(validate_templates.InvalidTemplateError):
        validate_templates.validate_file(json_file)


def test_missing_api_key(tmp_path):
    data = {"title": "t", "prompt": "p"}
    json_file = tmp_path / "tpl.json"
    json_file.write_text(json.dumps(data))
    if validate_templates.API_KEY_ENV in os.environ:
        del os.environ[validate_templates.API_KEY_ENV]
    with pytest.raises(validate_templates.MissingAPIKeyError):
        validate_templates.check_api_key()


def test_validate_directory_recursive_success(tmp_path):
    data = {"title": "t", "prompt": "p"}
    subdir = tmp_path / "sub" / "inner"
    subdir.mkdir(parents=True)
    json_file = subdir / "tpl.json"
    json_file.write_text(json.dumps(data))
    validate_templates.validate_directory(tmp_path)


def test_validate_directory_recursive_failure(tmp_path):
    data = {"title": "t"}
    subdir = tmp_path / "a" / "b"
    subdir.mkdir(parents=True)
    json_file = subdir / "tpl.json"
    json_file.write_text(json.dumps(data))
    with pytest.raises(validate_templates.InvalidTemplateError):
        validate_templates.validate_directory(tmp_path)
