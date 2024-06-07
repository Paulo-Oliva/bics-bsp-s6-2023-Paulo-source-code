from PIL import Image
import os


for image in os.listdir('.'):
    if not image.endswith('.png'):
        continue
    im = Image.open(image)
    print(im.format, im.size, im.mode)
    # If is png image
    if im.format == 'PNG':
        # and is not RGBA
        if im.mode != 'RGBA':
            im.convert("RGBA").save(f"./{image}")
            print(f"Converted {image} to RGBA")
