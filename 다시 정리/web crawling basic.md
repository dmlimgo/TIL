# 웹 크롤링 기초

터미널에서

```powershell
$ python #파이썬 실행
$ import webbrowser #웹을 실행가능하게 함
$ webbrowser.open('주소')
$ webbrowser.open('주소/search?=q검색어') #q는 querry의 약자
```

예제 - 한꺼번에 여러 검색 페이지 열기

```python
import webbrowser

idol=["아이유","윤아","둘리","태연"]
for x in idol:
    add="http://www.google.com/search?q="+x
    webbrowser.open(add)
    # time.sleep(3) # 3초 쉬었다가 실행
    # webbrowser.open(f"http://www.google.com/search?q={add})
    # webbrowser.open("http://www.google.com/search?q={}".format(member))
```

설치

```python
$ pip install requests # 뭐 요청 보내는 코드
$ pip install bs4 # 모듈	
```

- `requests` 요청을 대신 보내준다.
- `bs4`:문서를 파싱하는 것을 도와준다.

예제 - 코스피 지수 가져오기

1. 네이버에서 증권 페이지를 요청한다.
2. 페이지에서 내가 찾고 싶은 내용을 찾는다.

```python
import requests # s꼭 붙여야함
from bs4 import BeautifulSoup # bs4 중 Be~만 뽑아서 쓰겠다.

url = "https://finance.naver.com/sise/"
# 1. 원하는 사이트에 요청을 보낸다.
# 그리고 그 결과를 response에 저장한다.
response = requests.get(url)
# print(response.text)
# print(type(response))

# 2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text,'html.parser')
# BeautifulSoup 함수는 인자가 2개이다. 뒤의 인자는 html로 구조화 해준다.
# 3. Select는 CSS의 선택자(selector)을 통해 찾을 수 있다.
# KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
kospi = soup.select_one('#KOSPI_now')
print(kospi)
```

[추가자료참고](http://docs.python-requests.org/en/master/)