#!/bin/bash

# Directory containing the images
IMG_DIR="/home/atulj/mpksamiti/images/logos"

cd "$IMG_DIR" || exit

# Loop through all files starting with "WhatsApp"
for img in WhatsApp*.jpeg; do
    if [ -f "$img" ]; then
        echo "Running OCR on $img..."
        # This will output the result to a text file with the same name (e.g., file.jpeg -> file.txt)
        tesseract "$img" "${img%.jpeg}" -l hin+eng
    fi
done

echo "OCR completed. Text files have been generated in $IMG_DIR."
