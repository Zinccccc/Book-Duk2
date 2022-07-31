# Book-Duk2
독서 동호회 북덕북덕의 신청 도서를 자동으로 장바구니에 담아주는 프로그램

## prerequisite
|name|version|
|---|---|
|python|3.9.13|
|pip|22.1.1|
|Chrome|103.0.5060.134|

```
pip3 install tkinter
pip3 install pandas
pip3 install webdriver_manager
pip3 install openpyxl
pip3 install selenium
pip3 install bs4
```

macOS에서 tkinter가 설치되지 않는 경우, brew를 이용해 아래 명령어로 설치한다.
```
brew install python-tk
```

## How to use
1. 커맨드라인에서 아래 명령어로 실행
```
python3 Book-Duk2.py
```
2. 구매 신청 파일 선택
<img width="802" alt="Screen Shot 2022-07-31 at 10 57 44 AM" src="https://user-images.githubusercontent.com/5452969/182006467-4a67496b-212a-490c-a669-b681ee0717a9.png">
3. yes24 로그인
<img width="398" alt="Screen Shot 2022-07-31 at 10 58 29 AM" src="https://user-images.githubusercontent.com/5452969/182006469-5de4f992-9e06-4b07-a21e-1e7889087115.png">
4. 장바구니 확인
<img width="989" alt="Screen Shot 2022-07-31 at 11 00 18 AM" src="https://user-images.githubusercontent.com/5452969/182006480-ede5e631-617e-4185-9030-7334502a4387.png">
5. 로그 확인 
<img width="442" alt="Screen Shot 2022-07-31 at 11 00 47 AM" src="https://user-images.githubusercontent.com/5452969/182006482-d8e90a9f-890a-4300-983a-1310aa9b023d.png">
