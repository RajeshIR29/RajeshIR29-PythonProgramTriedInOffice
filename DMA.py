'''
1.Check filename exists or Not
2.if yes -
Open the file
form the query
move the file
3. we can give three more chance to enter the correct filename.
if all the chances are failed the exit the program
'''

import json
import os
import shutil
Minlimit=0
Maxlimit=3
try:
    while Minlimit < Maxlimit:

            location = "C:\\Dataset\\"
            filename=input("Enter the file name:")
            src_loc_file = location+filename
            arc_loc_file = location+"archive\\"+filename
            #print(loc_file)

            if os.path.exists(src_loc_file):
                #print(os.path.exists(src_loc_file))
                #fileopen=open(src_loc_file)
                #data=json.load(fileopen)
                with open(src_loc_file, "r") as file:
                    data = json.load(file)
                print(data)
                col1 = data["cols"][0]
                col2 = data["cols"][1]
                tablename = data["tablename"]
                where = data["where"]
                print(f"SELECT {col1},{col2} FROM {tablename} where {where}")
                shutil.move(src_loc_file,arc_loc_file)
                print("file processed successfully and moved to Archive")
                #fileopen.close()
                break
            else:
                Minlimit +=1
                print(f"please enter the proper filename or filename not available in the directory;You have left {Maxlimit - Minlimit} more chances ")
                if Maxlimit - Minlimit==0:
                    raise FileNotFoundError("File does not exist")
except FileNotFoundError as exceptiondesc:
    print(f"Given Chances are completed,Exception occurred {exceptiondesc}")
except Exception as exceptiondesc:
     print(f"Error Occurred {exceptiondesc}")
finally:
    print('program execution completed')