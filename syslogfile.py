import re, os

ids=[]
doc=input("enter document name here:")
with open ("C:\\Users\\USER\\Downloads\\"+ doc)as f:
      for line in f:
            if "TRACE"not in line:
                  continue
            pattern=r"\d+$"
            pattern2=r"^\d\d\d\d-\d\d-\d\d "
            word=re.search(pattern,line).group(0)
            match=re.search(pattern2,line).group(0)
            words=f"ids:{word} and date is :{match}"
            print(words)
      
        
