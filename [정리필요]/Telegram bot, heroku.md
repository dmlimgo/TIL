# 텔레그램 봇 만들기

> day5는 app.py set_rul.py 등등을 참고할것
>
> 그게 전부임

텔레그램+Flask 연결 -> 웹 훅(webhook)이용 

### 웹 훅

> 텔레그램 봇을 만들기 위해서 텔레그램에서 제공하는 웹 훅(web hook) 을 사용한다.
>
> 1. 사용자가 메세지 전송
> 2. 텔레그램 서버 - flask서버로 전달
> 3. flask 서버에서 처리 - 답장을 보냄

### 구현 기능

* 메아리 챗봇

  사용자가 보내준 메세지를 그대로 돌려줌

* 로또 챗봇

  `로또`라는 메세지를 보내면, 번호를 추천 해줌

* 번역 챗봇

  `/번역 ____`이 오면, 네이버 API를 통해서 번역된 값을 보내줌

* 유명인 닮은꼴(인식) 챗봇

  `사진`이 오면, 네이버 API를 통해서 닮은 사람을 말해줌

### 봇 만들기

telegram에서 BotFather에서 새로운 봇을 만들고 Token을 받는다.

### 환경변수로 설정하기

```powershell
$ vi ~/.bashrc
i 입력하여 수정모드로
export TELEGRAM_TOKEN="토큰"
```

```PYTHON
token = os.getenv("TELEGRAM_TOKEN")
```

##### bot API

https://core.telegram.org/bots/api#getting-updates참조

get webhook참조

```python

# flask 실행 명령어 : flask run --host=0.0.0.0 --port=8080
from flask import Flask
import os
app = Flask(__name__)

# 변수
c9_url = "https://telegram-bot-dmlim.c9users.io"
token = os.getenv("TELEGRAM_TOKEN")
api_url = f"https://api.telegram.org/bot{token}"
# api_url = f"https://api.telegram.org/bot{token}" 현재는 막혀있음?
set_webhook_url = f"{api_url}/SetWebhook?url={c9_url}/{token}"
print(set_webhook_url)

# request : 실제로 누가 나에게 보낸 걸 받을 때
# requests : 차이를 알자

@app.route(f'/{token}', methods=['POST'])
def telegram():
    return '성공', 200 # 상태 코드 404와 같음
# get = 요청을 하고 결과를 받는것, 주소창으로 감, 검색어 정도는 get으로 함

#method="post" 아이디 비밀번호 같은거 주소창으로 안보이게, 검색어 빼고는 대부분 post로 함
```

다 입력하고 터미널에

```:1st_place_medal:
$ flask run
```

입력하여 실행



##### 리스트를 문자열로

```:1st_place_medal:
"___".join("1","2")
```

1 ___2





##### heroku

무료 호스팅 지원

터미널에 pip install gunicorn

procfile 확장자 없이 파일 생성 후

```
web: gunicorn app:app
```

입력

$ gunicorn app:app

$ git init

$ git config --global user.name "dmlimgo"

$ git config --global user.email "dongmyeong.lim@gmail.com"

$ git add .

$ git commit -m "slfjlak"

$ ~~~

$ pip freeze > requirements.txt

하면 txt가 생김 pip로 깔았던거 볼 수 있음

$ git add .

$ git commit -m 'heroku settings'

$ heroku login

입력 후 아이디 비밀번호 입력

$ heroku creat myeong-telegram-bot

쓰면 주소가 나옴, 주소를 복사해서

어디다가 붙여놓을것

$ git push heroku master



오류나면?

- runtime.txt 파일 만들고 python-3.6.7입력

- $ git puch heroku master

위에서 나온 주소를 복사해서

set_url.py에서

```
if문 수정
if option == 1:
	url = "https://telegram-bot-dmlim.c9users.io"
elif option == 2:
	url = "https://taki-telegram-bot.herokuapp.com"
else:
	print("1,2 중에 고르라구!")
token = os.getenv("TELEGRAM_TOKEN")
api_url = f"http://api.telegram.org/bot{token}"
set_web~~은 같음
```



헤로쿠에서

프로젝트 Settings클릭 후 reveal config vars 클릭

bash열어서 `NAVER_CLIENT_ID`복사 붙여넣고 `ID`복사 붙여넣고

`NAVER_CLIENT_SECRET`복사 붙여넣고 `SECRET`복사 붙여넣고

그 밑에도 같이 복사하고 끝

끄려면 :q

ㅇ

터미널

python set_url.py

2

