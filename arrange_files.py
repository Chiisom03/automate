import os
import shutil

# Define categories and their corresponding file extensions
file_categories = {
    'document': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg'],
    'archive': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'executable': ['.exe', '.app', '.msi', '.sh', '.bat'],
    'font': ['.ttf', '.otf', '.woff', '.eot'],
    'database': ['.sqlite', '.db', '.mdb', '.csv', '.json'],
    'script': ['.py', '.js', '.php', '.html', '.css', '.rb'],
    'spreadsheet': ['.xls', '.xlsx', '.csv']
}


def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1].lower()

            # Find the category for the file
            file_category = None
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    file_category = category
                    break

            if file_category:
                destination_subfolder_path = os.path.join(
                    destination_folder, f"{file_category}s")

                if not os.path.exists(destination_subfolder_path):
                    os.makedirs(destination_subfolder_path)

                destination_path = os.path.join(
                    destination_subfolder_path, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_subfolder_path}'")


if __name__ == "__main__":
    source_folder = "enter/path/to/folder"
    destination_folder = "enter/path/to/folder"

    organize_files(source_folder, destination_folder)
