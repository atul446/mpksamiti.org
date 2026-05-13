import os

renames = {
    "WhatsApp Image 2026-05-12 at 7.15.09 PM": "विद्या_संस्कृति_साहित्य_एवं_कला_संरक्षण_केंद्र_बंडा_जिला_सागर_मध्य_प्रदेश",
    "॥॥_॥_॥॥॥॥": "श्री_विद्या_सामाजिक_न्याय_एवं_दिव्यांग_जन_सशक्तिकरण_केंद्र_बंडा_जिला_सागर_मध्य_प्रदेश",
    "A_९)_VA_RM_2_8,_24,_Ni_D,_A,_,_DI_ISTRICT_SA‘_GA": "श्री_विद्या_शिक्षा_एवं_प्रशिक्षण_केंद्र_बंडा_जिला_सागर_मध्य_प्रदेश"
}

base_dir = "/home/atulj/mpksamiti/images/logos"
ocrs_dir = os.path.join(base_dir, "ocrs")

for old_base, new_base in renames.items():
    # Rename jpeg
    old_jpeg = os.path.join(base_dir, old_base + ".jpeg")
    new_jpeg = os.path.join(base_dir, new_base + ".jpeg")
    if os.path.exists(old_jpeg):
        print(f"Renaming {old_jpeg} -> {new_jpeg}")
        os.rename(old_jpeg, new_jpeg)
        
    # Rename txt in ocrs/
    old_txt = os.path.join(ocrs_dir, old_base + ".txt")
    new_txt = os.path.join(ocrs_dir, new_base + ".txt")
    if os.path.exists(old_txt):
        print(f"Renaming {old_txt} -> {new_txt}")
        os.rename(old_txt, new_txt)
