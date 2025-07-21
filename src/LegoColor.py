class LegoColor:
    """Class to handle LEGO colors."""

    def __init__(self, rgb: tuple):
        """Initialize the LegoColor object with RGB values."""
        self.rgb = rgb

    def __eq__(self, other) -> bool:
        """Check if two LegoColor objects are equal."""
        if isinstance(other, LegoColor):
            return self.rgb == other.rgb
        return False

    def difference(self, other) -> float:
        """Calculate the difference between two LegoColor objects."""
        if isinstance(other, LegoColor):
            return sum(abs(a - b) for a, b in zip(self.rgb, other.rgb))
        return float('inf')

class LegoColorList:
    """Class to handle a list of LegoColor objects."""

    def __init__(self):
        """Initialize the LegoColorList."""
        self.colors = [LegoColor]

    def import_colors(self, path: str) -> list:
        """Import a list of colors."""
        colors = []
        try:
            with open(path, 'r') as file:
                for line in file:
                    line = line.split('#')[0].strip() # Remove hexa color and comments
                    if not line:
                        continue # Skip empty lines
                    rgb = tuple(map(int, line.strip().split(' ')))
                    colors.append(rgb)
        except FileNotFoundError:
            print(f"File '{path}' not found.")
        self.colors = colors
        return self.colors

    def __getitem__(self, index: int) -> LegoColor:
        """Get a color by index."""
        return LegoColor(self.colors[index])

    def __len__(self) -> int:
        """Return the number of colors."""
        return len(self.colors)
