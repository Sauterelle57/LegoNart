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
            print("\033[91mImage not opened yet.\033[0m")

    def downsample(self, size_x: int, size_y: int):
        """Downsample the image to the given size."""
        if self.img is not None:
            new_size = (size_x, size_y)
            self.img = self.img.resize(new_size, Image.Resampling.LANCZOS)
        else:
            print("\033[91mInvalid downsampling factor or image not opened.\033[0m")

    def convert_to_legocolors(self, color_path: str) -> list:
        """Convert the pixel values to LegoColor objects."""
        colors = LegoColorList().import_colors(color_path)
        if not colors:
            print("\033[91mNo colors imported. Please check the color file path.\033[0m")
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
            print("\033[91mNo Lego colors to generate the result image.\033[0m")
            return None

    def save(self, path: str):
        """Save the generated image to the specified path."""
        if self.result is not None:
            self.result.save(path)
        elif self.pixels is not None:
            self.pixels = self.pixels
        else:
            self.img.save(path)
            return
