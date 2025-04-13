from image_editor import ImageEditor

def main():
    path = input("Enter image path: ")
    editor = ImageEditor(path)

    while True:
        print("\nAvailable filters:")
        print("1. Brightness")
        print("2. Contrast")
        print("3. Blur")
        print("4. Black & White")
        print("5. Sharpen")
        print("6. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            factor = float(input("Enter brightness factor (e.g. 1.5): "))
            editor.apply("apply_brightness", factor)
        elif choice == "2":
            factor = float(input("Enter contrast factor (e.g. 1.5): "))
            editor.apply("apply_contrast", factor)
        elif choice == "3":
            editor.apply("apply_blur")
        elif choice == "4":
            editor.apply("apply_black_and_white")
        elif choice == "5":
            editor.apply("apply_sharpen")
        elif choice == "6":
            save_path = input("Enter path to save image: ")
            editor.save(save_path)
            print("Image saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

        editor.show()

if __name__ == "__main__":
    main()