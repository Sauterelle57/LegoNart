from PIL import Image
from LegoColor import LegoColor, LegoColorList
class LegoImage:
    def __init__(self, path: str):
        """Initialize the Image object with the path to the image file."""
        self.path = path
        self.img = None
        self.pixels = None
        self.pieces = []
        self.legocolors = []
        self.result = None

    def open(self):
        """Open the image file."""
        self.img = Image.open(self.path)

    def get_pixels(self) -> list:
        """Return the pixel values of the image."""
        if self.img is not None:
            self.pixels = list(map(lambda x: LegoColor(x[:3]), self.img.getdata()))  # Convert RGB to LegoColor
        return self.pixels

    def get_image_size(self) -> tuple:
        """Return the size of the image as (width, height)."""
        if self.img is not None:
            return self.img.size
        return (0, 0)

    def show(self):
        """Display the image."""
        if self.img is not None:
            self.img.show()
        else:
            print("Image not opened yet.")

    def downsample(self, factor: int = 0):
        """Downsample the image by the given factor."""
        if factor == 0:
            factor = min(self.img.size[0], self.img.size[1]) // 32
        if self.img is not None and factor > 0:
            new_size = (self.img.size[0] // factor, self.img.size[1] // factor)
            self.img = self.img.resize(new_size, Image.Resampling.LANCZOS)
        else:
            print("Invalid downsampling factor or image not opened.")

    def convert_to_legocolors(self, color_path: str) -> list:
        """Convert the pixel values to LegoColor objects."""
        colors = LegoColorList().import_colors(color_path)
        if not colors:
            print("No colors imported. Please check the color file path.")
            return []
        conversion_map = {}
        for pixel in self.pixels:
            if (pixel in conversion_map):
                self.legocolors.append(conversion_map[pixel])
                continue
            closest_color = min(colors, key=lambda c: pixel.difference(LegoColor(c)))
            self.legocolors.append(closest_color)
            conversion_map[pixel] = closest_color
        return self.legocolors

    def generate_result(self):
        """Generate a new image from the LegoColor objects."""
        if self.legocolors is not None:
            self.result = Image.new("RGB", self.get_image_size())
            self.result.putdata([color.get_value() for color in self.legocolors])
            return self.result
        else:
            print("No Lego colors to generate the result image.")
            return None

    def save(self, path: str):
        """Save the generated image to the specified path."""
        if self.result is not None:
            self.result.save(path)
            print(f"Image saved to '{path}'.")
        elif self.pixels is not None:
            self.pixels = self.pixels
            print(f"Image saved to '{path}'.")
        else:
            self.img.save(path)
            print(f"Image saved to '{path}'.")
            return
