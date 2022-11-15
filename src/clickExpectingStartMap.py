from src.utils import sleep_sec
import pyautogui as pag


#set fit position for cliking expected personal star-map
def get_expected_chartsTo_clipboard():

    pag.moveTo(1176, 549)

    sleep_sec(1)

    pag.doubleClick()

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

    #get expected report from that open from star-map

    pag.press('Enter')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    pag.press('tab')

    sleep_sec(1)

    #save as clipboard

    pag.press('Enter')

    sleep_sec(1)

    pag.press('Enter')

    sleep_sec(1)

