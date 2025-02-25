import numpy as np
from PIL import Image
import argparse
import os

try:
    import cairosvg  # Required for SVG support
    SVG_SUPPORTED = True
except ImportError:
    SVG_SUPPORTED = False


def image_to_npy(image_path, output_path):
    """Convert an image to a .npy file."""
    if image_path.lower().endswith(".svg"):
        if not SVG_SUPPORTED:
            print("CairoSVG is required for SVG conversion. Install it using: pip install cairosvg")
            return
        temp_png = "temp_image.png"
        cairosvg.svg2png(url=image_path, write_to=temp_png)
        image = Image.open(temp_png)
        os.remove(temp_png)  # Clean up temporary file
    else:
        image = Image.open(image_path)
    
    image_array = np.array(image)
    np.save(output_path, image_array)
    print(f"Image saved as .npy file at {output_path}")


def npy_to_image(npy_path, output_path):
    """Convert a .npy file back to an image."""
    image_array = np.load(npy_path)
    image = Image.fromarray(image_array)
    image.save(output_path)
    print(f".npy file converted to image and saved at {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert images (including SVG) to .npy and vice versa.")
    parser.add_argument("--mode", choices=["to_npy", "to_image"], required=True, help="Conversion mode")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")

    args = parser.parse_args()

    if args.mode == "to_npy":
        image_to_npy(args.input, args.output)
    elif args.mode == "to_image":
        npy_to_image(args.input, args.output)


if __name__ == "__main__":
    main()
