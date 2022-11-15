import pyautogui as pag
from constants import USERINFO
from src.utils import sleep_sec

def collecting_user_info():
    #opening new input area
    pag.press('f2')

    sleep_sec(3)

    pag.press('delete')

    sleep_sec(1)
    # it will be writing argument parser area for sys.argv
    # at the moment i will call from contants.py

    #taking name
    pag.write(f'{USERINFO.NAME}', interval=0.1)

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    #taking bithday
    pag.write(f'{USERINFO.DATE}', interval=0.1)

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    #taking birthtime
    pag.write(f'{USERINFO.TIME}', interval=0.1)

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    #taking birth place
    pag.write(f'{USERINFO.LOCATION}', interval=0.1)

    sleep_sec(1)

    pag.press('tab')

    #taking birth country
    sleep_sec(1)

    pag.write(f'{USERINFO.COUNTRYCODE}', interval=0.1)

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    #take gender selection

    if USERINFO.GENDER == "E":
        pag.press('down')
    elif USERINFO.GENDER == "K":
        pag.press('down')
        sleep_sec(1)
        pag.press('down')
    else:
        print("Lütfen geçerli bir girdi giriniz")

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('Enter')

