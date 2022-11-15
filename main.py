import pandas as pd
import time
from src.callSolarFire import start_solar_fire
from src.userInputs import collecting_user_info
from src.clickExpectingStartMap import get_expected_chartsTo_clipboard
from src.convertingInfoasDataframe import saveInfostoExcel
from constants import USERINFO
from src.config import CONFIG
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#def astrobot(): #it will be main function #test case'i yaz artık.

begin = time.time()

start_solar_fire()

collecting_user_info()

get_expected_chartsTo_clipboard()

saveInfostoExcel()

path = f"C:/Users/Asus/Desktop/solarFire/{USERINFO.NAME.replace(' ','_')}.xlsx"

df = pd.read_excel(f'{path}')

fin_time = (time.time() - begin) / 60

print(f"Programın çıktı süresi {fin_time} dakikadır. ")

print('beklemece')

#return df

#if __name__ == '__main__':
#    CONFIG.TEST = True
#    astrobot()
