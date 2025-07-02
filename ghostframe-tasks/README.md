# Ghostframe Tasks

Utility scripts for managing prompt templates and issue synchronization.

## Scripts

- **`convert_txt_to_json.py`** – Scan a directory for `.txt` files and produce a JSON file containing the filename and text content for each.
- **`validate_templates.py`** – Validate prompt templates (.json or .txt) ensuring required fields are present and any API keys are placeholders.
- **`sync_linear_issues.py`** – Example stub showing how repo issues might be synced to Linear. Requires `LINEAR_API_KEY` environment variable.

## Basic Usage

```bash
# convert all txt files in ./prompts to templates.json
python convert_txt_to_json.py ./prompts templates.json

# validate templates in ./prompts
python validate_templates.py ./prompts

# sync issues (stub)
LINEAR_API_KEY=your_token python sync_linear_issues.py
```

## deploy_checkpoints.json

This JSON file can be used to record commit hashes or other data for deployment checkpoints and validation status.
