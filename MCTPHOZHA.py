import time
import pyautogui
import random
import re



def mian():
    zi_dong_shua()
    
def zi_dong_shua():
    global speed
    speed = float(input("请输入打字的速度:"))
    speed_system = float(input("请输入输入指令的速度:"))
    pyautogui.PAUSE = speed_system
    while True:
        zhi_xin = input("发图片还是发文字:")
        if  zhi_xin == "文字":
            dao_ru = input("请选择\"导入文件文字\"或\"输入文件文字\":")
            if dao_ru== "输入文件文字":
                ma_ku = list()
                while True:
                    str_ing = input("输入你想骂的话加入骂人库:")
                    if str_ing != "继续":
                        ma_ku.append(str_ing)
                    else:
                        print(f"您加入{ma_ku}")
                        break
                ma_ren_xun(ma_ku)
            elif dao_ru == "导入文件文字":
                while True:
                    address = input("请输入文件地址:")
                    if re.match(r"^[a-zA-Z]:(\\[\w\u4e00-\u9fa5\s]+)+",address) != None:
                        print("输入地址正确")
                        with open(r"{}".format(address)) as z:
                            qie_ge = input("请输入切割字符:")
                            ma_ku = z.read().split(f"{qie_ge}")
                            print(f"您加入{ma_ku}")
                            ma_ren_xun(ma_ku)
                            break
                    else:
                        print("输入地址错误,请重新输入")
                        continue
        elif zhi_xin == "图片":
            while True:
                for i in range(int(input("请输入循环多少次:"))):
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press("enter")
                print("循环完成")
                if input("想在输入一遍请输入\"继续\":") != "继续":
                    break
            break
        else:
            print("没有这个东西")
        break

def ma_ren_xun(list_):
     while True:
        for i in range(int(input("请输入循环多少次:"))):
            time.sleep(2)
            shu_zi = random.randint(0,len(list_)-1)
            pyautogui.typewrite(list_[shu_zi],interval=speed)
            pyautogui.press("enter")
        print("循环完成")
        if input("想在输入一遍请输入\"继续\":") != "继续":
            break
            
mian()

