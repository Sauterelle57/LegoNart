from LegoImage import LegoImage
import time

def main(image_path, save_path="./results/result.png", size=(32, 32)):
    try:
        img = LegoImage(image_path)
        img.open()
        print(f"\033[93mProcessing...\033[0m")
        img.get_pixels()
        img.convert_to_legocolors("./resources/colors.txt")
        res = img.generate_result()
        res.save("./resources/intermediate_result.png")

        img = LegoImage("./resources/intermediate_result.png")
        img.open()
        img.downsample(size[0], size[1])
        img.save("./resources/intermediate_result2.png")
        img.get_pixels()
        print(f"\033[93mGenerating the result...\033[0m")
        img.convert_to_legocolors("./resources/colors.txt")
        img.generate_result()
        img.save(save_path)
        print(f"\033[92mImage successfully saved to '{save_path}'.\033[0m")

    except FileNotFoundError:
        print(f"\033[91mImage file '{image_path}' not found.\033[0m")


if __name__ == "__main__":
    start_time = time.time()

    image_path = input("Enter image path: ")
    save_path = input("Enter result path: (default: ./results/result.png) ") or './results/result.png'
    size_input = input("Enter result size (default: 32x32): ") or '32x32'
    size = tuple(map(int, size_input.split("x"))) if "x" in size_input else (32, 32)

    main(image_path, save_path, size)

    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")
