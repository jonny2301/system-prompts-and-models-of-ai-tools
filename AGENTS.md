# Repository guidelines

This repository collects system prompts and agent configuration files for a variety of AI tools. Each top-level folder corresponds to a specific project or tool. Examples include:

- `v0 Prompts and Tools` for Vercel's v0 prompts
- `Cursor Prompts` for the Cursor editor
- `Replit`, `Cluely`, `Lovable`, and others follow the same pattern

Prompt files are usually plain text (`.txt`) but some directories may also contain JSON or Markdown.

## Contribution instructions

1. Add new prompts to the folder that matches the tool's name. If no folder exists, create a new one at the repository root with a clear name.
2. Keep file names short and descriptive.
3. Avoid modifying existing prompts unless absolutely necessary.
4. Pull requests should describe the files you added or changed.

## Continuous integration

This project has minimal CI requirements. If you modify JavaScript or TypeScript files, run:

```bash
npm run lint
npm test -- --watchAll=false
```

If `package.json` or `requirements.txt` is changed, install dependencies with `npm install` or `pip install -r requirements.txt` before committing.

## License

All files in this repository are provided under the terms of the GNU General Public License version 3 (GPLv3). See `LICENSE.md` for details.
