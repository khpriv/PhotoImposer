from pickletools import optimize

from PIL import Image, ImageOps
import pathlib


def open_images_resize_save():
    p = pathlib.Path("IN")
    for images in p.iterdir():
        filename = images.name

        with Image.open(f"IN/{filename}") as im:
            height = min(im.size)
            if height != im.height:
                im.rotate(90)

            if im.width <= int(im.height * 1.4):
                im = ImageOps.fit(im, [im.width, int(im.width / 1.4)], centering=[0.5, 0.5])
            else:
                im = ImageOps.fit(im, [int(im.height * 1.4), im.height], centering=[0.5, 0.5])
                print("else")

            justname = filename.split()[0]
            im.save(f"OUT/{justname}_resized", "JPEG", quality=90)


if __name__ == '__main__':
    open_images_resize_save()
