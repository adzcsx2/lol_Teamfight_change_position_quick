# 生成exe
# pyinstaller.exe -F --i icon.ico main.py
import sys
import time
sys.path.append("E:\\python_workplace\\yundinghuanwei\\venv\\lib\\site-packages")
import pyautogui as pag
from pynput import keyboard
from pynput.mouse import Button, Controller
offset_1 = 900
offset_2 = 960
mouse = Controller()
def move(offset, x, y):
    off = abs(offset - x)
    if x < offset:
        x = x + 2 * off
        click(x,y)
    else:
        x = x - 2 * off
        click(x, y)
    print("在棋盘内，移动棋子到：",x,y)


def click(x, y):
    pag.moveTo(x, y)
    mouse.click(Button.left)


def on_press(key):
    # 键盘按下
    print("按下了{}".format(key))


def on_release(key):
    try:
        if (key == keyboard.Key.space):
            x, y = pag.position()  # 返回鼠标的坐标
            print("按下空格，坐标 :",x,y)
            mouse.click(Button.left)
            time.sleep(0.1)
            if y > 400 and y < 490 or y > 550 and y < 640:
                move(offset_1, x, y)
            if y > 490 and y < 550 or y > 640 and y < 720:
                move(offset_2, x, y)
            time.sleep(0.1)
            pag.moveTo(x, y)#还原位置
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        print("按下了esc")
        # return False


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as  listener:
            listener.join()

