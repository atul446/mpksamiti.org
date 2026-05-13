import os
import glob

dir_path = "/home/atulj/mpksamiti/images/various_parts_of_samiti"
ocrs_dir = os.path.join(dir_path, "ocrs")

prefix_mappings = {
    "एवं_निःशुल्क_वरिष्ठ_जन_आवास_गृह": "विद्या_छाया_सर्वसुविधायुक्त_सशुल्क_एवं_निःशुल्क_वरिष्ठ_जन_आवास_गृह_बंडा",
    "कार्यक्रम_ढिनांक_स्थान_प्रायोजक": "विद्या_संस्कृति_साहित्य_एवं_कला_संरक्षण_केन्द्र_बंडा",
    "खेल_बंडा_मातृ_पितृ_कृपा": "श्री_विद्याकुंज_खेल_अकेडमी_बंडा",
    "छा_विद्या_आयोजक_मातृ_पितृ": "विद्या_संस्कृति_साहित्य_एवं_कला_संरक्षण_केन्द्र_बंडा",
    "छाया_पर्यावरण_आयोजक": "विद्या_छाया_पर्यावरण_संरक्षण_केन्द्र",
    "मातृ_पितृ_कृपा_शैक्षिक": "श्री_विद्याकुंज_स्पेशल_स्कूल_बंडा",
    "विद्या_कृपा_नशाबंदी_एवं": "विद्या_कृपा_नशाबंदी_एवं_नशामुक्ति_प्रचार_प्रसार_केन्द्र_बंडा",
    "विद्या_कृपा_नशामुक्ति_केन्द्र": "विद्या_कृपा_नशामुक्ति_एवं_पुनर्वास_केन्द्र_बंडा",
    "विद्या_छाया_सर्वभुविधायुक्त_सशुह्क_एवं_निःशुल्क_वरिष्ठ": "विद्या_छाया_सर्वसुविधायुक्त_सशुल्क_एवं_निःशुल्क_वरिष्ठ_जन_आवास_गृह_बंडा",
    "विद्या_स्वास्थ्य_केन्द्र_आयोजक": "विद्या_स्वास्थ्य_केन्द्र",
    "हि_श्री_विद्या_बाल_विकास": "श्री_विद्या_बाल_विकास_एवं_सशक्तिकरण_केन्द्र",
    "॥_कि_आयोजक_मातृ_पितृ": "श्री_विद्या_शिक्षा_एवं_प्रशिक्षण_केन्द्र"
}

# Keep track of used names to avoid immediate collisions during this run
used_names = set()

jpeg_files = glob.glob(os.path.join(dir_path, "*.jpeg"))

for jpeg_path in jpeg_files:
    old_filename = os.path.basename(jpeg_path)
    old_basename = os.path.splitext(old_filename)[0]
    
    new_basename = None
    for prefix, new_name in prefix_mappings.items():
        if old_basename.startswith(prefix):
            new_basename = new_name
            break
            
    if not new_basename:
        print(f"No mapping found for {old_filename}")
        continue
        
    # Find a unique new name
    final_basename = new_basename
    counter = 1
    while final_basename in used_names or os.path.exists(os.path.join(dir_path, final_basename + ".jpeg")):
        final_basename = f"{new_basename}_{counter}"
        counter += 1
        
    used_names.add(final_basename)
    
    new_jpeg_path = os.path.join(dir_path, final_basename + ".jpeg")
    old_txt_path = os.path.join(ocrs_dir, old_basename + ".txt")
    new_txt_path = os.path.join(ocrs_dir, final_basename + ".txt")
    
    print(f"Renaming {old_filename} -> {final_basename}.jpeg")
    os.rename(jpeg_path, new_jpeg_path)
    
    if os.path.exists(old_txt_path):
        os.rename(old_txt_path, new_txt_path)
