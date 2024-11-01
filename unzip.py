import zipfile
import os

with zipfile.ZipFile(r'archive.zip', 'r') as zip_file:
    zip_file.extractall(path='dataset/')