from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR2 = Path(__file__).resolve().parent
# BASE_DIR3 = Path(__file__).resolve()
print(BASE_DIR)
# print(BASE_DIR2)
# print(BASE_DIR3)

# FILE_UPLOAD_TEMP_DIR = os.path.abspath(os.path.join(BASE_DIR, 'mysite2', 'temp'))
# print(FILE_UPLOAD_TEMP_DIR)
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'mysite2', 'static'))
print(STATIC_ROOT)

# FILE_UPLOAD_TEMP_DIR = r'd:\mysite2\mysite2\temp'
# print(FILE_UPLOAD_TEMP_DIR)
