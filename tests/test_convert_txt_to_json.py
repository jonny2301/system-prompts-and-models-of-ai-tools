import json
from pathlib import Path
from ghostframe_tasks import convert_txt_to_json

def test_txt_to_json(tmp_path: Path):
    txt_file = tmp_path / "sample.txt"
    txt_file.write_text("Title\nThis is a prompt")
    json_path = convert_txt_to_json.txt_to_json(txt_file)
    data = json.loads(json_path.read_text())
    assert data["title"] == "Title"
    assert data["prompt"] == "This is a prompt"
