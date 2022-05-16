#!/usr/bin/python

import subprocess

result = subprocess.run(['ls', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
app_list =result.stdout.split('\n')
# apk start from apk_list[3]


def install_app(apk_list):
    for i in range(3,len(apk_list)-1):
        print(apk_list[i])
        try:
            task = subprocess.run(["adb", "install", apk_list[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
            print(str(task.stdout))
        except:
            print(task.stderr)
            return False
    return True

print('-- How to use this? --')
how = """

Just place this file inside the folder containing *ONLY APKs* to install
then make sure you have the appropriate permissions for adb and device.
Just run it as python3 adb-install.py


"""
print(how)
isGo = input("Type 'yes'/'no' to continue : " )
if isGo == "yes":
    installed = install_app(app_list)
    if installed:
        print("All Done! Bye Bye!")
else:
    print('Okay then, See ya later!')

