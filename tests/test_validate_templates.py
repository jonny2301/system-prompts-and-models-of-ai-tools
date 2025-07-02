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
