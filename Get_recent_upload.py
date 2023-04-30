import os
from pathlib import Path
import sys
stud_cl=int(input("Enter class name:\n1)1st_M.sc_CS\n2)2nd_M.sc_CS"))
if(stud_cl==1):
    stud_cls="1st_M.sc_CS"
elif stud_cl==2:
    stud_cls="2nd_M.sc_CS"
else:
    print("Invalid")
    sys.exit(1)
folder_path = Path(f"C:/Users/Srini/Desktop/srini/{stud_cls}/")
file_list = os.listdir(folder_path)
recent_file = None
max_time = 0
for file_name in file_list:
    try:
        file_time = os.path.getctime(folder_path / file_name)
        if file_time > max_time:
            max_time = file_time
            recent_file = file_name
    except OSError:
        pass
if recent_file is not None:
    print("The most recently created file is:", recent_file)
else:
    print("No files found in the folder. Try insert files first!")
