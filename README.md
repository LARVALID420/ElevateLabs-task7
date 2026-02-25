# Task 7 – Batch Image Resizer Tool

A Python script that **resizes and converts images in bulk** using the Pillow library.


- Scans a folder for images (JPG, PNG, BMP, GIF, TIFF, WEBP)
- Resizes every image to a target size (default **800 × 800 px**)
- Optionally converts images to a different format (e.g. JPG → PNG)
- Preserves aspect ratio by default (no stretching)
- Saves results to a separate output folder

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
