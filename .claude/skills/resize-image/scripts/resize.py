import sys
import os
from PIL import Image

def main():
    if len(sys.argv) != 4:
        print("Usage: python resize.py <input_path> <output_path> <WIDTHxHEIGHT>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    resolution_str = sys.argv[3]

    if not os.path.exists(input_path):
        print(f"Error: Input file does not exist: {input_path}")
        sys.exit(1)

    try:
        width_str, height_str = resolution_str.lower().split('x')
        target_width = int(width_str) if width_str else None
        target_height = int(height_str) if height_str else None
    except ValueError:
        print(f"Error: Invalid resolution format. Expected WIDTHxHEIGHT, xHEIGHT or WIDTHx. Got: {resolution_str}")
        sys.exit(1)

    try:
        print(f"Opening {input_path}...")
        img = Image.open(input_path)

        # Load the image fully before we do operations to prevent reading errors on save
        img.load()

        print(f"Original size: {img.size}")
        orig_w, orig_h = img.size

        # Support proportional scaling if only one dimension is provided
        if target_width is None and target_height is not None:
            target_width = int(orig_w * (target_height / orig_h))
        elif target_height is None and target_width is not None:
            target_height = int(orig_h * (target_width / orig_w))

        if orig_w == 0 or orig_h == 0 or target_width == 0 or target_height == 0:
             print("Error: Target width and height must be > 0")
             sys.exit(1)

        # If output and input path are same, save to temp file first to prevent reading from empty file
        temp_output_path = output_path
        if os.path.abspath(input_path) == os.path.abspath(output_path):
            temp_output_path = output_path + ".tmp.resize"

        # Use LANCZOS for high-quality downsampling if available, otherwise fallback
        resample_filter = getattr(Image, 'Resampling', Image).LANCZOS
        resized_img = img.resize((target_width, target_height), resample=resample_filter)

        # Ensure output directory exists
        output_dir = os.path.dirname(os.path.abspath(output_path))
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
            if resized_img.mode in ("RGBA", "P"):
                resized_img = resized_img.convert("RGB")

        if temp_output_path != output_path:
            # Tell PIL what format to use explicitly since .resize extension might be unknown
            ext = os.path.splitext(output_path)[1].lower()
            format_map = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".gif": "GIF", ".bmp": "GIF", ".webp": "WEBP"}
            fmt = format_map.get(ext, None)
            resized_img.save(temp_output_path, format=fmt)
        else:
            resized_img.save(output_path)

        if temp_output_path != output_path:
            import shutil
            shutil.move(temp_output_path, output_path)

        print(f"Successfully saved {target_width}x{target_height} image to {output_path}")
        img.close()
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()