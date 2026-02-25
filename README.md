# Task 7 – Batch Image Resizer Tool

A Python script that **resizes and converts images in bulk** using the Pillow library.

## What it does
- Scans a folder for images (JPG, PNG, BMP, GIF, TIFF, WEBP)
- Resizes every image to a target size (default **800 × 800 px**)
- Optionally converts images to a different format (e.g. JPG → PNG)
- Preserves aspect ratio by default (no stretching)
- Saves results to a separate output folder

## Tools / Libraries
| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pillow (`PIL`) | Open, resize, and save images |
| `os` module | Read files from directory |

## How to run

### 1. Install Pillow
```bash
pip install Pillow
```

### 2. Put your images in a folder called `images/`
```
project/
├── image_resizer.py
├── images/          ← place your original images here
└── images_resized/  ← resized images appear here (auto-created)
```

### 3. Run the script
```bash
python image_resizer.py
```

### 4. Customise (optional)
Open `image_resizer.py` and edit the settings at the bottom:

```python
INPUT_FOLDER  = "images"          # source folder
OUTPUT_FOLDER = "images_resized"  # output folder
TARGET_SIZE   = (800, 800)        # target width x height
OUTPUT_FORMAT = None              # None = keep original, or "PNG" / "JPEG"
KEEP_RATIO    = True              # True = keep aspect ratio
```

## Key concepts covered
- **File Handling** – listing directory contents with `os.listdir()`
- **Image Processing** – opening, resizing, and saving images with Pillow
- **Format Conversion** – changing file extensions / formats on the fly
- **Error Handling** – `try-except` blocks to skip corrupt or unsupported files

## Interview Q&A (quick reference)

| Question | Answer |
|----------|--------|
| What is PIL/Pillow? | Pillow is a Python imaging library for opening, manipulating, and saving image files. |
| How do you open/save images? | `Image.open(path)` and `img.save(path, format=...)` |
| What is `resize()`? | Resizes an image to an exact (width, height); `thumbnail()` is similar but keeps aspect ratio. |
| How do you read all files in a directory? | `os.listdir(folder)` returns a list of filenames. |
| What is the `os` module? | A standard library module for interacting with the operating system (paths, directories, etc.). |
| How to change formats? | Save with a different extension and pass `format="PNG"` (or "JPEG") to `img.save()`. |
| What is a pixel? | The smallest unit of a digital image; each pixel holds colour information. |
| Why use try-except? | To catch errors on corrupt/unsupported files without crashing the whole batch. |
| How to make it dynamic? | Accept command-line arguments (`argparse`) or add a simple GUI (Tkinter). |
| Can it be extended to GUI? | Yes — Tkinter lets users browse folders and pick settings visually. |
