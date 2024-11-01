import os
import shutil

def delete_file(path: str):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        # Check if the item is a file
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)  # Remove file
                print(f"Removed file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove directory and its contents
                print(f"Removed directory: {item_path}")
        except Exception as e:
            print(f"Error removing {item_path}: {e}")
