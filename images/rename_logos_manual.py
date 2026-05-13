import os

# Dictionary mapping old filenames to new Hindi filenames
renames = {
    "WhatsApp Image 2026-05-12 at 7.15.06 PM.jpeg": "मातृपितृकृपा_शैक्षिक_स्वास्थ्य_पर्यावरण_खेल_संबंध_सामाजिक_विकास_और_कल्याण_समिति_बांदा.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.07 PM (1).jpeg": "विद्या_छाया_सर्वसुविधायुक्त_सशुल्क_एवं_निःशुल्क_वरिष्ठजन_आवास_गृह_बंडा_सागर.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.08 PM (1).jpeg": "श्री_विद्याकुंज_स्पेशल_स्कूल_बंडा_जिला_सागर_मध्य_प्रदेश.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.08 PM.jpeg": "विद्या_कृपा_नशा_मुक्ति_एवं_पुनर्वास_केंद्र_बंडा_जिला_सागर_मध्य_प्रदेश.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.09 PM (1).jpeg": "श्री_विद्याकुंज_खेल_अकादमी_बंडा_जिला_सागर.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.09 PM (2).jpeg": "विद्या_कृपा_नशा_बंदी_एवं_नशा_मुक्ति_प्रचार_प्रसार_केंद्र_बंडा_जिला_सागर_मध्य_प्रदेश.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.10 PM (1).jpeg": "विद्या_स्वास्थ्य_केंद्र_जिला_सागर_मध्य_प्रदेश.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.10 PM.jpeg": "विद्या_छाया_पर्यावरण_संरक्षण_केंद्र_बंडा_जिला_सागर.jpeg",
    "WhatsApp Image 2026-05-12 at 7.15.11 PM.jpeg": "श्री_विद्या_बालविकास_एवं_महिला_सशक्तिकरण_केंद्र_बंडा_जिला_सागर.jpeg"
}

dir_path = "/home/atulj/mpksamiti/images/logos"

for old_name, new_name in renames.items():
    old_path = os.path.join(dir_path, old_name)
    new_path = os.path.join(dir_path, new_name)
    
    if os.path.exists(old_path):
        print(f"Renaming {old_name} -> {new_name}")
        os.rename(old_path, new_path)
    else:
        print(f"Skipped {old_name} - Not found")
