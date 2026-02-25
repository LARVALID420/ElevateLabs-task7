"""
Task 7: Batch Image Resizer Tool
---------------------------------
Resizes and converts all images in a folder using Python + Pillow.
Usage:
    python image_resizer.py
Or customize the settings at the bottom of this file.
"""

import os
from PIL import Image


def resize_images(
    input_folder: str,
    output_folder: str,
    size: tuple = (800, 800),
    output_format: str = None,   # e.g. "PNG", "JPEG", or None to keep original
    keep_aspect_ratio: bool = True
):
    """
    Resize (and optionally convert) every image found in input_folder.

    Parameters
    ----------
    input_folder     : path to the folder that contains the source images
    output_folder    : path where resized images will be saved
    size             : target (width, height) in pixels
    output_format    : force a specific format ("PNG", "JPEG", …) or None to keep original
    keep_aspect_ratio: if True uses thumbnail-style resizing (never upscales beyond size)
    """

    # Supported image extensions
    SUPPORTED = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read every file in the input folder
    files = os.listdir(input_folder)
    if not files:
        print(f"No files found in '{input_folder}'.")
        return

    processed = 0
    skipped = 0

    for filename in files:
        name, ext = os.path.splitext(filename)
        if ext.lower() not in SUPPORTED:
            print(f"  [SKIP] {filename}  — not a supported image format")
            skipped += 1
            continue

        input_path = os.path.join(input_folder, filename)

        # Determine output extension / format
        fmt = output_format.upper() if output_format else ext.lstrip(".").upper()
        # Pillow uses "JPEG" not "JPG"
        if fmt == "JPG":
            fmt = "JPEG"
        out_ext = ".jpg" if fmt == "JPEG" else f".{fmt.lower()}"
        output_filename = name + out_ext
        output_path = os.path.join(output_folder, output_filename)

        try:
            with Image.open(input_path) as img:
                # Convert palette/RGBA images to RGB when saving as JPEG
                if fmt == "JPEG" and img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                if keep_aspect_ratio:
                    img.thumbnail(size, Image.LANCZOS)   # shrinks in-place, keeps ratio
                else:
                    img = img.resize(size, Image.LANCZOS)

                img.save(output_path, format=fmt)
                print(f"  [OK]   {filename}  →  {output_filename}  {img.size}")
                processed += 1

        except Exception as e:
            print(f"  [ERROR] {filename}: {e}")
            skipped += 1

    print(f"\nDone! {processed} image(s) resized, {skipped} skipped.")
    print(f"Output saved to: {os.path.abspath(output_folder)}")


# ──────────────────────────────────────────────
#  SETTINGS — change these to suit your needs
# ──────────────────────────────────────────────
if __name__ == "__main__":
    INPUT_FOLDER  = "images"          # folder with your original images
    OUTPUT_FOLDER = "images_resized"  # folder where results will be saved
    TARGET_SIZE   = (800, 800)        # max width x max height (pixels)
    OUTPUT_FORMAT = None              # None = keep original | "PNG" | "JPEG" | etc.
    KEEP_RATIO    = True              # True = preserve aspect ratio

    resize_images(
        input_folder=INPUT_FOLDER,
        output_folder=OUTPUT_FOLDER,
        size=TARGET_SIZE,
        output_format=OUTPUT_FORMAT,
        keep_aspect_ratio=KEEP_RATIO
    )
