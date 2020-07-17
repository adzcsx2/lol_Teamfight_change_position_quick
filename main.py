# 生成exe
# pyinstaller.exe -F --i icon.ico main.py
import time
import pyautogui as pag
from pynput import keyboard
from pynput.mouse import Button, Controller
screen1080 = 0
offset_1080 = [900,960]
offset_768 = [645,685]
mouse = Controller()
grid_1080 = [[420,470],[490,540],[570,620],[650,700]]
grid_768 = [[300,330],[355,385],[405,435],[465,495]]

grid = []
offset = []

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
        grid = []
        offset = []
        if screen1080 == "1":
            grid = grid_1080
            offset =offset_1080
        elif screen1080 == "0":
            grid = grid_768
            offset = offset_768

        if (key == keyboard.Key.space):
            x, y = pag.position()  # 返回鼠标的坐标
            print("按下空格，坐标 :",x,y)
            mouse.click(Button.left)
            time.sleep(0.1)
            print(grid[0][0])
            if y > grid[0][0] and y < grid[0][1] or y > grid[2][0] and y < grid[2][1]:
                move(offset[0], x, y)
            if y > grid[1][0] and y < grid[1][1] or y > grid[3][0] and y < grid[3][1]:
                move(offset[1], x, y)
            time.sleep(0.1)
            pag.moveTo(x, y)#还原位置
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        print("按下了esc")
        # return False


if __name__ == "__main__":
    print("屏幕分辨率1080*1920输入1,，768*1366输入0：",flush=True)
    screen1080 = input()
    print("ok")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as  listener:
            listener.join()
