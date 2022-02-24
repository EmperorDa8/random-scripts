from pathlib import Path
import sys

textfolder=[]
csvfolder=[]
jsonfiles=[]
jpgfiles=[]
pngfiles=[]
totalfiles=[]

sys_path=sys.argv[1]

def arrange_files(sys_path):
    files_path=Path(sys_path)
    grand=files_path.iterdir()
# for loop to list files in in directory into a list 
    for file in grand:
        totalfiles.append(file)
        print(totalfiles)
        # this loop iterate through the above list and sort according to their extension
        for x in totalfiles:
    
            if x.suffix == ".csv":
                csvfolder.append(x.name)
            elif x.suffix == ".json":
                jsonfiles.append(x.name)
            elif x.suffix == ".txt":
                textfolder.append(x.name)
            elif x.suffix == ".png":
                pngfiles.append(x.name)
            elif x.suffix == ".jpg":
                jpgfiles.append(x.name)
            else:
                pass
            print("process done!")
            return csvfolder, jsonfiles, textfolder, pngfiles, jpgfiles


    