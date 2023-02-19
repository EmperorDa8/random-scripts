from pathlib import Path
import sys

def arrange_files(sys_path):
    file_extensions = {
        ".csv": [],
        ".json": [],
        ".txt": [],
        ".png": [],
        ".jpg": []
    }
    
    files_path = Path(sys_path)
    for file in files_path.iterdir():
        if file.suffix in file_extensions:
            file_extensions[file.suffix].append(file.name)
    
    print("Process done!")
    return file_extensions[".csv"], file_extensions[".json"], file_extensions[".txt"], file_extensions[".png"], file_extensions[".jpg"]

if __name__ == "__main__":
    csv_files, json_files, txt_files, png_files, jpg_files = arrange_files(sys.argv[1])
    print(csv_files, json_files, txt_files, png_files, jpg_files)

            return csvfolder, jsonfiles, textfolder, pngfiles, jpgfiles


    
