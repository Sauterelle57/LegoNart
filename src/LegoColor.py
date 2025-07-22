class LegoColor:
    """Class to handle LEGO colors."""

    def __init__(self, rgb: tuple, name: str = ""):
        """Initialize the LegoColor object with RGB values."""
        self.rgb = rgb
        self.name = name

    def __eq__(self, other) -> bool:
        """Check if two LegoColor objects are equal."""
        if isinstance(other, LegoColor):
            return (self.rgb, self.name) == (other.rgb, other.name)
        return False

    def __hash__(self):
        return hash((self.rgb, self.name))

    def difference(self, other) -> float:
        """Calculate the difference between two LegoColor objects."""
        if isinstance(other, LegoColor):
            return sum(abs(a - b) for a, b in zip(self.rgb, other.rgb))
        return float('inf')

    def get_value(self) -> tuple:
        """Return the RGB value of the LegoColor."""
        return self.rgb

    def get_name(self) -> str:
        """Return the name of the LegoColor."""
        return self.name

    def __len__(self) -> int:
        """Return the length of the RGB tuple."""
        return len(self.rgb)

    def __iter__(self):
        return iter(self.rgb)

    def __str__(self) -> str:
        """Return a string representation of the LegoColor."""
        return f"LegoColor(rgb={self.rgb}, name='{self.name}')"


class LegoColorList:
    """Class to handle a list of LegoColor objects."""

    def __init__(self):
        """Initialize the LegoColorList."""
        self.colors = [LegoColor]

    def import_colors(self, path: str) -> list:
        """Import a list of colors."""
        legocolors = []
        try:
            with open(path, 'r') as file:
                for line in file:
                    color, name = line.split('#')
                    if not line:
                        continue # Skip empty lines
                    name = name.split('(')[1].split(')')[0].strip() if '(' in name and ')' in name else name
                    color = color.strip()
                    color = tuple(map(int, color.split(' ')))
                    legocolors.append(LegoColor(color, name))
        except FileNotFoundError:
            print(f"File '{path}' not found.")
        self.colors = legocolors
        return self.colors

    def __getitem__(self, index: int) -> LegoColor:
        """Get a color by index."""
        return self.colors[index]

    def __len__(self) -> int:
        """Return the number of colors."""
        return len(self.colors)

    def __str__(self) -> str:
        """Return a string representation of the LegoColorList."""
        return f"LegoColorList(colors={self.colors})"
