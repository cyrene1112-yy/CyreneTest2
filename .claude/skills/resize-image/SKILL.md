---
name: resize-image
description: "Use this skill whenever you need to resize, scale, or change the resolution of an image file. Give it an input path, output path, and target dimensions (e.g., widthxheight)."
---

# Resize Image Skill

You have a Python script to resize images reliably.

Whenever the user asks you to resize an image, use the script provided in this skill's `scripts` directory.

### Usage

Run the following command using the Bash tool to resize the image. Since Pillow may not be installed globally, you can run the script via a python command that ensures dependencies are handled, or you can suggest the user install Pillow if it fails:

```bash
python3 .claude/skills/resize-image/scripts/resize.py "<input_path>" "<output_path>" "<target_resolution>"
```

- `<input_path>`: The absolute or relative path to the image you want to resize.
- `<output_path>`: The absolute or relative path where the resized image should be saved.
- `<target_resolution>`: The target resolution in the format `WIDTHxHEIGHT` (e.g., `1920x1080` or `800x600`).

### Example

If the user says: "Resize `assets/bg/my_bg.png` to 1280x720 and save it as `assets/bg/my_bg_resized.png`"

You should run:
```bash
python .claude/skills/resize-image/scripts/resize.py "assets/bg/my_bg.png" "assets/bg/my_bg_resized.png" "1280x720"
```

If it succeeds, tell the user the image has been resized. If it fails due to missing dependencies, you might need to run `pip install Pillow` first.