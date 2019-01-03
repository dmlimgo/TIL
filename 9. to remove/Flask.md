# Flask

[공식 홈페이지](http://flask.pocoo.org)

### 1. 설치하기

먼저 터미널에서 flask 폴더를 만들고 (윈도우에서 만들어도 됨)

```powershell
$ pip install flask
```

vs code에서 hello.py를 만들고 flask 홈페이지의 Flask is Fun 내용을 복사 저장

flask 홈페이지의 And Easy to Setup의 두번째 줄 복사해서 터미널에 입력. 주소를 복사해서 확인하면 됨.

##### 예제

크리스마스인가? 확인하는 페이지

```python
from flask import Flask
import datetime # 사용법 참조
app = Flask(__name__) # Flask라는 애를 만듬

@app.route("/") # /경로
def hello():
    return "Hello World!"

@app.route("/ssafy") # 경로 추가
def ssafy():
    return "datetime.now()"
# 수정 후에는 서버 재부팅해야함.

@app.route("/isitchristmas")
def christmas():
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    if month==12 and day ==25:
        return "네"
    else:
        return "아니오"
```

- 홈페이지를 연결해보자
- flask 폴더 안에 templates 폴더를 만들고( 약속임 지켜줘야함 ) 그안에 index.html을 만들어 준다.
- html:5 하고 tap누르면 자동완성

- `<a ''>`링크를 도와줌

- `render_template`를 사용하면 html 파일에서 변수, 조건, 반복문 등을 활용할 수 있다. `jinja2`라고하는 템플릿 엔진을 활용하고 있기 때문이다.
- 기본적으로 html파일은 `templates/`폴더 안에 만들어야 한다.

```html
<!-- templates/dinner.html -->
{{menu}} <!-- 출력을 원할 경우 {{ }}를 활용한다. -->
{% if __ %}
	<h1>참이면</h1> <!-- 제어문을 활용할 경우 {% %}를 활용한다. -->
	<h1>보인다</h1>
{% else %}
	<h1>거짓이면</h1>
	<h1>보인다</h1>
{% end if %}

{% for i in menus %}
	<p>{{i}}</p>
{% endfor %}
```





- {% %}는 주석처리가 안되니 주의

이미지 업로드

- w3school이 괜찮음 - HTML Images참조
- 이미지 업로드 할 때는 우클릭 - 이미지 주소 복사를 해야함
- 동영상은 동영상 공유 눌러서 나온 주소를 해야함

```python
from flask import Flask, render_template
import datetime
import random
import os
app = Flask(__name__) # Flask라는 애를 만듬

@app.route("/") # /경로
def hello():
    return render_template("index.html") #특정한 html파일을 지정해 줄 수 있음

@app.route("/ssafy") # 경로 추가
def ssafy():
    return "datetime.now()"
# 수정 후에는 서버 재부팅해야함.

@app.route("/isitchristmas")
def christmas():
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    if month==12 and day ==25:
        return "네"
    else:
        return "아니오"


# variable routing - url에서 변수 활용
@app.route("/greeting/<string:name>")
def greeting(name): #윗 줄의 name위치랑 같은 변수여야 함
    return f"{name}야(아) 안녕"
# name 입력에 따라 다른 페이지 나옴

@app.route("/cube/<int:numb>")
def cube(numb):
    result = numb*numb*numb
    return f"{result}" # 숫자 반환은 안되더라

@app.route("/dinner")
def dinner():
    # 1. 저녁 list 만들고
    dinner_list = ["까르보나라","곰탕","닭갈비","라멘","가츠동"]
    # 2. 하나 뽑아주세요
    menu = random.choice(dinner_list)
    return render_template("dinner.html",menu = menu, dinner = dinner_list) # 나가서(html에서) 쓸 이름=여기서 쓰는 이름


@app.route("/merrychristmas")
def merrychristmas():
    url = "https://youtu.be/DHy1iKBtTq4"
    img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK3coa3-Iktw-SzOemJngv5mfLK0g6G6ZvflOZARg-TuanfYSb"
    return render_template("merrychristmas.html",url=url,img=img)

```

index.html

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Myeong's project</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <a href="/dinner">저녁메뉴추천받기!</a> <!--내 페이지에서 하는거라 주소 다 할필요 없음 -->
        <a href="/isitchristmas">크리스마스일까?</a>
        <a href="/merrychristmas">메리크리스마스</a>
    </body>
</html>
```

dinner.html

```html
 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Document</title>
 </head>
 <body>
     <h1>{{menu}} 먹어!!</h1>
     {% if menu == "곰탕" %} <!-- if문이라 for문등을 표시할 때 쓰는 표현-->
        <h2>오늘은 굶자... 곰탕이 뭐냐...</h2>
     {% else %}
        <h2>맛점!!!!</h2>
     {% endif %} <!--약속이므로 써주자-->
     <hr> <!-- 수평선 -->
     저녁 리스트는 이거였어.
     {% for food in dinner %}
        {{food}}
     {% endfor %}
 </body>
 </html>
```

merrychristmas.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>document</title>
    <h1>ooo</h1>
</head>
<body>
    <h1>ddlink</h1>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/DHy1iKBtTq4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <img src="dance.png">
    <img src="{{img}}">
</body>
</html>
```

