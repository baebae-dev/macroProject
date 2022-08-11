# 마우스 x,y 축을 알아내는 방법

import pyautogui
import keyboard
import time

while 1:
    position = pyautogui.position()
    if keyboard.is_pressed('enter'):
        print(position)
        time.sleep(0.2)

# 해당 소스코드는 왼쪽클릭을 하는경우 좌표가 출력되는 방식이다
# pyautogui의 단점은 입력에 관한 함수가 없기 때문에 enter키를 누르면 나오게 설정하였다