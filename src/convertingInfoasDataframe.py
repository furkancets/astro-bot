import os
from src.utils import sleep_sec
import pyautogui as pag
from constants import USERINFO
import pyperclip
import pandas as pd

def saveInfostoExcel():

    # opening excel =>> in future need to expoler different converting type to pandas dataframe
    os.startfile(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')

    sleep_sec(3)

    pag.press('Enter')

    sleep_sec(1)

    # copy and save operation
    with pag.hold('ctrl'):
       pag.press('v')

    sleep_sec(2)

    with pag.hold('ctrl'):
       pag.press('s')

    sleep_sec(2)

    pag.write(f'{USERINFO.NAME.replace(" ","_")}')
    sleep_sec(2)

    pag.press('Enter')
    sleep_sec(2)

    #s = pyperclip.paste()
    #with open(f'{USERINFO.NAME.replace(" ","_")}.txt', 'w', encoding="utf8", errors='ignore' ) as g:
        #g.write(s)

    #dataset = pd.read_csv(f'{USERINFO.NAME.replace(" ","_")}.txt', delimiter="\t")
    #print(dataset)
    #print("a")