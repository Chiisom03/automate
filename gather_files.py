import os
import shutil

source_folder = "enter/path/to/folder"
destination_folder = "enter/path/to/folder"


def gather_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for category_folder in os.listdir(source_folder):
        category_folder_path = os.path.join(source_folder, category_folder)

        if os.path.isdir(category_folder_path):
            for filename in os.listdir(category_folder_path):
                source_path = os.path.join(category_folder_path, filename)
                destination_path = os.path.join(destination_folder, filename)

                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_folder}'")


if __name__ == "__main__":
    gather_files(source_folder, destination_folder)
