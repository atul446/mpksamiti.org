import os
import glob
import re

directories = [
    "/home/atulj/mpksamiti/images/various_parts_of_samiti",
    "/home/atulj/mpksamiti/images/logos"
]

def clean_hindi_filename(text):
    # Keep only Devanagari characters (U+0900 to U+097F) and whitespace
    hindi_only = re.sub(r'[^\u0900-\u097F\s]', ' ', text)
    
    # Replace newlines with spaces
    hindi_only = hindi_only.replace('\n', ' ').replace('\r', ' ')
    
    # Replace multiple spaces with a single underscore
    hindi_only = re.sub(r'\s+', '_', hindi_only)
    hindi_only = hindi_only.strip('_')
    
    # Truncate to avoid OS limit (150 bytes)
    encoded = hindi_only.encode('utf-8')
    if len(encoded) > 150:
        hindi_only = encoded[:150].decode('utf-8', 'ignore')
        
    return hindi_only.strip('_')

for d in directories:
    txt_files = glob.glob(os.path.join(d, "*.txt"))
    for txt_path in txt_files:
        base_name = os.path.splitext(txt_path)[0]
        jpeg_path = base_name + ".jpeg"
        
        if not os.path.exists(jpeg_path):
            continue
            
        with open(txt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_name_base = clean_hindi_filename(content)
        
        # If no Hindi text was found, skip
        if not new_name_base or len(new_name_base) < 2:
            print(f"Skipping {os.path.basename(jpeg_path)} - No valid Hindi text found.")
            continue
            
        new_jpeg_path = os.path.join(d, new_name_base + ".jpeg")
        new_txt_path = os.path.join(d, new_name_base + ".txt")
        
        # If it's already named this, skip
        if new_jpeg_path == jpeg_path:
            continue
            
        counter = 1
        while os.path.exists(new_jpeg_path) and new_jpeg_path != jpeg_path:
            new_jpeg_path = os.path.join(d, f"{new_name_base}_{counter}.jpeg")
            new_txt_path = os.path.join(d, f"{new_name_base}_{counter}.txt")
            counter += 1
            
        if new_jpeg_path != jpeg_path:
            print(f"Renaming:\n  {os.path.basename(jpeg_path)} -> {os.path.basename(new_jpeg_path)}")
            os.rename(jpeg_path, new_jpeg_path)
            os.rename(txt_path, new_txt_path)
