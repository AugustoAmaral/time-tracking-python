from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import csv


def saveFile(data_object):
    with open('used_programs.csv', mode='w') as used_programs:
        writer = csv.writer(used_programs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Program window', 'Time using in seconds'])
        for key in data_object:
            writer.writerow([key, data_object[key]])


print("Hello!, This program will store all used programs on csv file.")
print("With this, we can find out how productive we are being!")
print('Close the program to finish it from running')

used_programs = {}

while True:
    sleep(1)
    program_name = GetWindowText(GetForegroundWindow())
    try:
        used_programs[program_name] = used_programs[program_name] + 1
    except:
        used_programs[program_name] = 1
    saveFile(used_programs)
