import os
import PyInstaller.__main__
import shutil

from pathlib import Path

# delete old build in dist folder
output_folder = Path('./dist')

# delete output folder
for filename in os.listdir(output_folder):
    file_path = os.path.join(output_folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path} Reason: {e}")

# build executable from spec file
PyInstaller.__main__.run([
    'main.spec',
    '-D',  # one folder bundle that contains executable
    '--noconsole'
])
