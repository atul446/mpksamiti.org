import os

def get_files_in_dir(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(file)
    return sorted(list(set(file_names)))

docs_files = get_files_in_dir("/home/atulj/mpksamiti/docs")
image_files = get_files_in_dir("/home/atulj/mpksamiti/images")

with open("/home/atulj/mpksamiti/project_requirement.txt", "a") as f:
    f.write("\n\n### Document Files Available (docs/):\n")
    for doc in docs_files:
        f.write(f"- {doc}\n")
        
    f.write("\n### Image Files Available (images/):\n")
    for img in image_files:
        f.write(f"- {img}\n")

print("Successfully appended file names to project_requirement.txt")
