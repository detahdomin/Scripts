from pynput import mouse
import pyautogui
# 移动监听
pan=False
def on_move(x, y):
    print('鼠标移动到了：{}'.format((x, y)))
 
# 点击监听
def on_click(x, y, button, pressed):
    print('鼠标按键：{}，在位置处 {}, {} '.format(button, (x, y), '按下了' if pressed else '释放了'))
    global pan
    if pressed == 1 and pan==0:
        pan=True
    if pan:
        for _ in range(60):
            pyautogui.typewrite('1')
            pyautogui.hotkey('Enter')
    listener.stop()
 
# 滚动监听
def on_scroll(x, y, dx, dy):
    print('滚动中... {} 至 {}'.format('向下：' if dy < 0 else '向上：', (x, y)))
 
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

listener.start()
listener.join()


1
1
1
1
1
1
1
1
1
