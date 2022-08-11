# 정지기능 추가
import pyautogui
import keyboard
import time

while 1:
    pyautogui.press('f5', interval=3)
    print('I want to go IU concert!!')

    pyautogui.click(x=757, y=858, interval=0.1)
    pyautogui.click(x=766, y=737, interval=0.1)
    pyautogui.click(x=864, y=811, interval=0.1)
    pyautogui.click(x=582, y=632, interval=0.1)
    pyautogui.click(x=651, y=645, interval=0.1)
    pyautogui.click(x=647, y=654, interval=0.1)
    pyautogui.click(x=841, y=856, interval=0.1)
    pyautogui.click(x=684, y=800, interval=0.1)
    pyautogui.click(x=608, y=759, interval=0.1)
    pyautogui.click(x=629, y=679, interval=0.1)
    pyautogui.click(x=890, y=747, interval=0.1)
    pyautogui.click(x=741, y=712, interval=0.1)

    if keyboard.is_pressed('f12'):
        break
    # 루프문 탈출
    # f5후 해당위치 3곳을 클릭한다.