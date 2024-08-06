import os
from pathlib import Path
 
# get current directory
APP_BASE_DIR = os.getcwd()
APPFILES = os.path.join(APP_BASE_DIR, 'appfiles')
xls_filename = os.path.join(APPFILES, 'TM_CIs_Associated_Service.xlsx')

print(xls_filename)


BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)