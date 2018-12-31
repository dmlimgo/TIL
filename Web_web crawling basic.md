# 웹 크롤링 기초

[TOC]

---



### 1. 코드를 이용해 웹페이지 열기

#### 1) 웹 접근 명령어

```powershell
$ python #파이썬 실행
$ import webbrowser #웹을 실행가능하게 함
$ webbrowser.open('주소')
$ webbrowser.open('주소/search?=q검색어') #q는 querry의 약자
```

#### 2) 예제 - 한꺼번에 여러 검색 페이지 열기

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



### 2. 웹 크롤링

#### 1) 필요한 파일 설치하기

```python
$ pip install requests 	# 뭐 요청 보내는 코드
$ pip install bs4 		# 모듈	
```

- `pip` : Python Intalls Packages
- `requests` : 요청을 대신 보내준다.
- `bs4`: 문서를 파싱하는 것을 도와준다.

#### 2) 명령어

```python
import requests
requests.get('URL') # URL에 요청을 보낸 결과를 리턴함.
# s꼭 붙여야함.
# request와 requests는 다름.

BeautifulSoup(정보,'html.parser')
이 함수는 인자가 2개이다. 뒤에 인자는 html로 구조화(파싱) 해준다
```

#### 3) 크롤링을 위한 웹 조사하기

[참고사이트](https://blog.naver.com/timtaeil/221420471952)

* 웹페이지에서 원하는 부분 우클릭 > 검사 > CSS페이지에서 우클릭 > copy > copy selector

* 구조를 이해해서 어떤 부분을 써야 원하는 데이터를 얻을 수 있을지 생각하자

#### 4) 예제 - 코스피 지수 가져오기

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
# ex) id='contentarea'
kospi = soup.select_one('#KOSPI_now')
print(kospi)
# 구조는 제외하고 텍스트만 출력
print(kospi.text)
```

[requests 원문](http://docs.python-requests.org/en/master/)

* `css` : Cascading Style Sheets
* `BeautifulSoup` : 컴퓨터가 잘 찾기 위해 형식을 바꿔주는 것
* `soup.select` : 여러개를 리스트 형태로
* `soup.select_one` : 리스트 중 첫번째 것

#### 5) 예제 - 네이버 검색어 순위 가져오기

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
keyword = soup.select('.ah_roll')
lists = keyword[0].select('.ah_k')
# list의 성격을 잘 보고 []를 이용해야할지를 알아야 함.

for idx, word in enumerate(lists,1):
    print(idx, word.text)
```

* `enumerate(리스트)` : 순서가 있는 자료형(tuple, list, string)을 첫번째 인자로 받아서 각각의 index값과 value값들을 enumerate 객체로 리턴함.

  두 번째 인자로 정수를 전달하면 시작하는 index값 조정 가능.



### 기타

[공공데이터 포털](data.go.kr) > 오픈 API만 쓴다.(파일형식은 못 써먹음)