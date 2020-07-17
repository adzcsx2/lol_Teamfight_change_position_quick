import win32com.client
import pyautogui as pag

dm = win32com.client.Dispatch('dm.dmsoft')

x, y = pag.position()
pos = [x - 50, y - 50, 100, 100]
# dm_ret = dm.Capture(x-50,y-50,x+50,y+50,"screen.bmp")
# print(dm_ret)

a,b = 0,0
dm_ret = dm.FindMulColor(x-50,y-50,x+50,y+50,"feda25",0.9)
print(dm_ret)
if a>0 or b>0:
    print("找到")

dm_ret = dm.FindPic(x-50,y-50,x+50,y+50,"E:\python_workplace\yundinghuanwei/feature.bmp","202020",0.5,0,a,b)
# print(dm_ret)

if a>0 or b>0:
    print("找到")