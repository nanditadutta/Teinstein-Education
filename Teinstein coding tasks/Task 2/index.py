from datetime import date
from datetime import timedelta
from datetime import datetime

import os


def taskfunction(url, x):
    file1 = open(url, "r+")
    inputstr = file1.readlines()
    publishDate = inputstr[0][17:27].replace("-", "/")
    inputText = inputstr[1]
    # print(publishDate)
    sysdate = date.today().strftime("%d/%m/%Y")
    # print(sysdate)

    if(str(publishDate) != str(sysdate)):
        tod = datetime.strptime(publishDate, "%d/%m/%Y")
        yes = tod - timedelta(days=1)
        tom = tod + timedelta(days=1)
        print(str(tod))
        # print(yes)
        # print(tom)
        inputText = inputText.replace("today", "on "+str(tod)[:9])
        inputText = inputText.replace("Today", "On "+str(tod)[:9])
        inputText = inputText.replace("tomorrow", "on "+str(tom)[:9])
        inputText = inputText.replace("Tomorrow", "On "+str(tom)[:9])
        inputText = inputText.replace("yesterday", "on "+str(yes)[:9])
        inputText = inputText.replace("Yesterday", "On "+str(yes)[:9])

    print(inputText)

    file2 = open("output"+x, "w+")
    file2.write(inputText)

    file1.close()
    file2.close()


path = r""
os.chdir(path)

for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"

        # call read text file function
        print(file_path)
        taskfunction(file_path, file)
