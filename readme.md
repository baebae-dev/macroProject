# 실행환경
환경 : 가상환경 생성 후 동작 (패키지 충돌 방지)
언어 : Python

# 실행 방법
```
# 1. 필수 패키지 등 설치
pip install -r requirements.txt

# 2. 실행할 위치좌표 찾기
# Mac은 관리자 권한으로 실행해야함.
# 키보드 관련 기능에 있어 You can't run a script with virtual keyboard inputs like you regular python file in the macOS terminal due to a security feature.
sudo python3 getPosition.py

# 살행 후 클릭할 곳을 클릭하여 위치 정보 알아냄. 
# (venv)  ✘ bell.coco@bellcocoui-MacBookPro  ~/PycharmProjects/pythonProject  sudo python3 getPosition.py
# Point(x=1105, y=840)

# 3. 마우스 매크로 설정
# 2에서 찾아낸 위치를 지정해야함.
sudo python3 getPosition.py

```