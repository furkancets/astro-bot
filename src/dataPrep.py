import pandas as pd
from constants import USERINFO

path = f"C:/Users/Asus/Desktop/solarFire/{USERINFO.NAME.replace(' ','_')}.xlsx"

df = pd.read_excel(f'{path}')

#set numeric columns

columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

df.columns = columns

print(df.columns)

if USERINFO.GENDER == "K":
    print("Female")
else:
    print("Male")

house_cups = pd.DataFrame(pd.concat([df[16:19][1], df[16:19][4], df[16:19][7], df[16:19][10]], ignore_index=True))
house_cups["index"] = [int(i.strip()[0:2]) for i in house_cups[0]]

planets = df[22:36][[1, 2]].reset_index(drop=True)
