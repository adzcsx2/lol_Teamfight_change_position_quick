import cv2
import numpy as np
import pyautogui
import pyautogui as pag

ImageFileName = "aa.bmp"
FeatureFileName = "feature.bmp"
def templateMacthing(src, template, method):
    result = cv2.matchTemplate(src, template, method)
    threshold = 0.8
    location = np.where(result >= threshold)
    print(location[1])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # location = [0, 0]
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    return location

def find_picture(target,template):
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(max_val)
    print(strmin_val)
    #绘制矩形边框，将匹配区域标注出来
    #min_loc：矩形定点
    #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),1)
    #显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    x=min_loc[0]
    y=min_loc[1]

    return x,y

def take_screen():
    x, y = pag.position()
    pos = [x - 50, y - 50, 100, 100]
    img = pyautogui.screenshot(region=pos)  # x,y,w,h
    img.save(ImageFileName)

# 截屏鼠标附近
take_screen()

template=cv2.imread(ImageFileName)
target= cv2.imread(FeatureFileName)

x,y = find_picture(target,template)
print(x,y)
#
# lower_gold = np.array([216,187,36])
# upper_gold = np.array([254,227,40])
#
# src = cv2.imread(ImageFileName, 1)
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, lower_gold, upper_gold)
# cv2.imshow('Mask', mask)
# print(mask)

# template = cv2.imread(FeatureFileName, 1)
# methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]
# locations = []
# for method in methods:
#     locations.append(templateMacthing(src, template, method))
#     print(locations)


#
# # 1.读入原图和模板
# img_rgb = cv2.imread(ImageFileName)
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread(FeatureFileName, 0)
# h, w = template.shape[:2]
#
# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
#
# loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
# for pt in zip(*loc[::-1]):  # *号表示可选参数
#     right_bottom = (pt[0] + w, pt[1] + h)
#     cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
# #
# # print(result)
# # mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# # print('mn_val',mn_val)
# # print('max_val',max_val)
# # print('min_loc',min_loc)
# # print('max_loc',max_loc)
