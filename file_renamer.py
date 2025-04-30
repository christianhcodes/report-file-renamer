
import os
import datetime

INPUT_FOLDER = "raw_reports"
OUTPUT_FOLDER = "renamed_reports"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

files = os.listdir(INPUT_FOLDER)
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

for idx, filename in enumerate(files, start=1):
    name, ext = os.path.splitext(filename)
    new_name = f"{date_str}_Report_{idx:03}{ext}"
    src_path = os.path.join(INPUT_FOLDER, filename)
    dst_path = os.path.join(OUTPUT_FOLDER, new_name)
    if os.path.isfile(src_path):
        with open(src_path, "rb") as f_in:
            content = f_in.read()
        with open(dst_path, "wb") as f_out:
            f_out.write(content)

print("Files have been renamed and copied to 'renamed_reports'.")
