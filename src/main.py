from LegoImage import LegoImage
import time

def main():
    image_path = "./resources/sources/ironman.jpg"
    save_path = "./resources/results/ironman_result_64_64.png"
    try:

        img = LegoImage(image_path)
        img.open()
        img.get_pixels()
        img.convert_to_legocolors("./resources/colors.txt")
        res = img.generate_result()
        res.save("./resources/intermediate_result.png")

        img = LegoImage("./resources/intermediate_result.png")
        img.open()
        img.downsample(9)
        img.save("./resources/intermediate_result2.png")
        img.get_pixels()
        img.convert_to_legocolors("./resources/colors.txt")
        img.generate_result()
        img.save(save_path)

    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")
