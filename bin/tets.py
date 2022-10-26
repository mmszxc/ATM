import os
import re
import shutil

target = 'C:\\\作业\\'
for first_dirname, send_dirname, file_name in os.walk(r'C:\三江\1-30'):

    for line in file_name:

        res = first_dirname.strip().split('\\')
        # res[-2]  day27
        day_dir = res[-2]

        if "作业" in line:

            # print(line)
            aaa = day_dir+line
            #
            # shutil.copy(os.path.join(first_dirname,line),target)
            # os.rename(os.path.join(first_dirname,line),os.path.join(target,aaa))
