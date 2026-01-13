import os
from desktop_path import get_desktop_path
from process_image import process_image
from error_message_box import show_error


def main():
    desktop_path = get_desktop_path()
    scanner_folder = os.path.join(desktop_path, "scanner")

    if not os.path.exists(scanner_folder):
        show_error(
            "A pasta 'scanner' não foi encontrada na Área de Trabalho.\n\n"
            "Crie a pasta e coloque as imagens dentro dela."
        )
        return

    for file_name in os.listdir(scanner_folder):
        if not file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(scanner_folder, file_name)

        key = process_image(image_path)

        if key:
            new_name = f"{key}.jpg"
            new_path = os.path.join(scanner_folder, new_name)

            if not os.path.exists(new_path):
                os.rename(image_path, new_path)


if __name__ == "__main__":
    main()
