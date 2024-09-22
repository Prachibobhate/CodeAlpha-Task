import os
import shutil

# Define the source directory (replace with your actual path)
source_dir = 'C:/Users/Prachi/Downloads'

# Define the destination directories (replace with your actual paths)
destination_dirs = {
    'Documents': 'C:/Users/Prachi/Documents',
    'Images': 'C:/Users/Prachi/Pictures',
    'Spreadsheets': 'C:/Users/Prachi/Spreadsheets',
}

# File extensions to look for
file_types = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.gif'],
    'Spreadsheets': ['.xlsx', '.csv'],
}

# Organize files based on their extensions
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if any(filename.endswith(ext) for ext in extensions):
                shutil.move(file_path, destination_dirs[category])
                break

# Optional: Delete empty folders
for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)

print("File organization complete.")
