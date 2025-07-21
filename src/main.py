from LegoImage import LegoImage

def main():
    image_path = "./resources/baboon.jpg"
    try:
        img = LegoImage(image_path)
        img.open()
        img.get_pixels()
        img.convert_to_legocolors("./resources/colors.txt")
        res = img.generate_result()
        res.save("./resources/intermediate_result.png")

        img = LegoImage("./resources/intermediate_result.png")
        img.open()
        img.downsample()
        img.get_pixels()
        img.convert_to_legocolors("./resources/colors.txt")
        img.generate_result()
        img.save("./resources/baboon_result_32_32.png")

    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")

if __name__ == "__main__":
    main()
