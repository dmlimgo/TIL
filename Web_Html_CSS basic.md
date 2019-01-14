# HTML/CSS 기초

[TOC]

### 0) 들어가기 전에

* 첫줄에 <!Doctype html>이라고 쓴다. 요샌 안해도 되는데 이게 기본
* visual studio code에 3가지 추가기능 설치 
  * `HTML snippets` : for, while 등과 같이 재사용 가능한 코드들의 모음.
  * `HTML CSS Support` : CSS 지원인듯
  * `Auto Close Tag` : close tag(ex.</html>)를 자동으로 붙여주는 기능
* IP (Internet Protocal) : 8비트 숫자로 구성된 숫자의 집합. 각자가 가지고 있는 주소와 동일
* 도메인 : 네트워크상으 ㅣ컴퓨터를 ㅣ식별하는 호스트명
* URL (Uniform Resource Locator) : 도메인 + 경로 실제로 해당서버에서 자원이 어디 있는지 알려주기 위한 고유 규약
* HTML (Hyper Text Markup Language) : Hyper text -> 하이퍼링크 같은거
* HTTP (Hyper Text Transfer Protocol) : 규약
* alt 누르고 이동하면 움직임

### 1) 기본 구조

```html
<!Doctype html>
<html>
    <head>
        <!-- 문서의 정보를 담고 있다. -->
        <title>네이버</title> <!-- 탭에 표시되는 이름 -->
    </head>
    <body>
        <!-- 문서의 내용을 담고있다. 실제로 브라우저에서 보이는 내용들 -->
        <!-- paragraph -->
        <p>
            본문
        </p>
    </body>
</html>
```

* `html:5`로도 생성 가능

### 2) CSS

CSS (Cascading Sytle Sheets)의 약자, HTML과 같은 마크업 언어를 꾸며준다.

꾸며주기 위해서 특정한 태그를 선택해야 하는데 이때 이용되는 것이 `CSS 선택자(Selector)`이다.

```html
<h1> 안녕? 제목이니 </h1>
# 마크다운과 동일
```

```html
<title> 네이버 </title>
# 탭 이름이 바뀜
```

```html
# 인라인 속성
<h1 style="color:red;">안녕? 제목이니?</h1>
```

```html
 .red{
                color:red;
            }
# class가 red인 친구를 다 찾아서 color를 red로 설정
```

```html
선택자들
.red{}	#class
#blue{} #id
p{}		#tag
우선순위 inline>id>class>tag
**color:skyblue!important; 가 가장 우선
```

```html
<!Doctype html>
<html>
    <head>
        <title> 네이버 </title>
        <style>
            .red{
                color:red;
            }
            #blue {
                color:blue;
            }
            p {
                color: skyblue;
            }
        </style>
    </head>
    <body>
        <h1 style="color:red;">안녕 제목이니</h1>
        <p class="red"> 빨간색 ?</p>
        <p id="blue">파란색</p>
        <p> 무슨색</p>
    </body>
</html>
```

#### 2.1 css 없애보기

 크롬 확장 프로그램 -> web developer 다운로드

아무 웹사이트 들어가서 css disable



### 3) HTML

#### 3.1 Tag와 Dom tree

##### 3.1.1 요소

```html
<h1>
</h1>
```

Tag는 대소문자를 구별하지 않으나 소문자로 작성해야 한다. 요소간에 중첩 가능

##### 3.1.2 안닫는태그?

```html
<img src="url"/>
```

닫는 태그가 없는 태그도 존재

##### 3.1.3 속성

```html
<a href='google.com'/>
  #속성명 #속성값
```

##### 3.1.4 DOM 트리 (Document Object Model)

```html
<body>
    <h1>    </h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
# body태그와 h1태그는 부모(parent)-자식(child) 관계
# li태그는 형제 관계(sibling)
```

##### 3.1.5 시맨틱 태그

> 컨텐츠에 의미를 설명하는 태그
>
> 검사(F12) 찍어보면 앎
>
> 단순히 보여주기를 넘어서 ''의미를 가지는 태그를 활용''하기 위해 사용

| 태그    | 설명                                                         |
| ------- | ------------------------------------------------------------ |
| header  | 헤더(문서 전체나 섹션의 헤더)                                |
| nav     | 내비게이션(메뉴 같은거)                                      |
| aside   | 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용 |
| section | 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현 h1~h6 요소를 가짐. |
| article | 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역 (포럼 신문 등의 글 또는 기사) |
| footer  | 푸터 (문서 전체나 섹션의 푸터, 문서나 섹션의 하단)           |

###### 3.1.5.1 NAVER 뉴스와 GOOGLE 뉴스 어느것이 갓인가

각각의 홈페이지 접속 후 > Web Developer > information > View Document Outline

문서가 어떻게 구조화 되어 있는지 볼 수 있음

###### 3.1.5.2 SEO (검색 엔진 최적화)

#### 3.2 HTML 만들어보기

##### 3.2.1 디자인 룰

 * =을 붙여씀
 * '보다는 "를 씀

##### 3.2.1 마크업

###### 3.2.1.1 스크롤 만들기

```html
<head>
    <style>
        body{
            height: 10000px;
        }
    </style>
</head>
```

###### 3.2.1.2 표 선 굵기, 색상 조절

```html
<head>
    <style>
        table, tr, td{
            border:1px solid darkolivegreen
        }
    </style>
</head>
```

###### 3.2.1.3 문단, 글자 꾸미기

```html
<!-- 빈줄 추가 (엔터를 인식하지 않는다. p태그를 쓰면 자동으로 주바꿈) -->
<br>

<!-- 선긋기 -->
<hr>

<!-- 굵은 글씨 -->
<b>lorem</b>impum
<strong>lorem</strong>ipsum

<!-- 이탤릭체 -->
<i>lorem</i>ipsum
<em>lorem</em>ipsum

<!-- 취소선을 나타냅니다. -->
<del>취소선을 나타냅니다.</del>

<!-- 하이라이팅도 가능합니다. -->
<mark>하이라이팅</mark>도 가능합니다.

<!-- 아랫첨자 -->
log<sub>10</sub>10

<!-- 윗첨자 -->
2<sup>3</sup>

<!-- 띄어쓰기를 많이 해도 한칸만 인식하므로 -->
<p>아                               아!</p>
<!-- &nbsp(non breaking space)를 입력해줘야함 -->
<p>아&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp아!</p>
```



```html
    <body>
        <h1 id="heading">heading1</h1>

        <!-- pre는 띄어쓰기나 문자를 있는 그대로 사용하기 위해서 씀 -->
        <!-- typora의 ```와 비슷하게 동작한다 -->
        <pre id="q">
            import random
            random.sample(range(1, 46),6)
            띄   어   쓰       기
        </pre>
        <!-- 인용문 사용 -->
        <q>인녕핫요, 잉용문입니다. 짧을 때 사용하세요.</q>
        <!-- blockquote는 typora의 > 와 비슷하게 동작 -->
        <blockquote>인용문이지만, 긴 문장입니다.
            아마도 들여쓰기가 기본적으로 적용됩니다.
        </blockquote>
        <!-- Typora 에서 리스트 형식으로 작성할 때 태그 -->
        <!-- ul(unordered list) -->
        <ul>
            <li>순서가 없습니다.</li>
            <li>이재찬</li>
            <li>박성민</li>
        </ul>
        <!-- ol(ordered list) -->
        <ol>
            <li>1교시</li>
            <li>2교시</li>
        <!-- 태그이름*숫자 하면 갯수만큼 생성 됨 -->
        <!-- ctrl + alt 하면 세로줄로 동시에 작업가능 -->
            <li>3교시</li>
            <li>4교시</li>
            <li>5교시</li>
            <li>6교시</li>
        </ol>
        <!-- ul>li*3처럼 하면 형식대로 생성 됨 -->
        <!-- emmet 기능임 -->
        <!-- style을 적용해보자 -->
        <ul>
            <li style="list-style-type: square">사과</li>
            <li>바나나</li>
            <li>안녕!</li>
        </ul>
        <a href = "https://google.com" target="_blank">새 창에서 구글로</a>
        <!-- self가 default -->
        <a href = "https://google.com" target="_self">여기에서 구글로</a>
        <!-- 원하는 곳에 가고 싶으면 id선택자를 사용한다. 위에 id="heading"을 쓰고 -->
        <a href = "#heading">상단으로</a>
        <a href = "#q">인용문으로</a>
        <a href = "hello.html" target="_blank">hello, world</a>
    </body>
</html>
```

##### 3.2.2 사이트

html5test.com

internet live stats

[혼자 웹 공부 - 웹 개발 가이드](https://developer.mozilla.org/ko/)

##### 3.2.3 style

[스타일 가이드](https://www.w3schools.com/cssref/pr_list-style-type.asp)

```html
<li style="list-style-type: none">CSS</li>
<li style="list-style-type: lower-alpha">CSS</li>
```

##### 3.2.4 input

[input type attribute](https://www.w3schools.com/tags/att_input_type.asp)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        body{
            height:10000px;
        }
    </style>
</head>
<body>
    <h2>Form input</h2>
    <form action="#">
        <!-- name : 변수로 넘어감, value : 입력값 혹은 출력값 -->
        <!-- placeholder는 사용자 경험 측면에서 별로 권장하지 않는 방법임 -->
        일반텍스트 : <input name="username" type="text" placeholder="이름을 입력해 주세요" autofocus><br>
        이메일 : <input type="email" placeholder="이메일을 입력해 주세요" autocomplete><br>
        비밀번호 : <input type="password" placeholder="비밀번호를 입력해 주세요"><br>
        날짜 : <input type="date"><br>
        숨겨서 사용자 모르게 처리할 수 있음 : <input type="hidden" value="이 사람은 바보"><br>
        <input type="button" value="버튼~"><br>
        <input type="submit" value="서브밋~"><br>
        <!-- radio button -->
        <input type="radio" name="gender" value="male"> 남자
        <input type="radio" name="gender" value="female" checked> 여자<br>
        <!-- checkbox -->
        <input type="checkbox" name="option" value="1"> SIA <br>
        <input type="checkbox" name="option" value="2"> QUEEN <br>
        <input type="checkbox" name="option" value="3"> travis <br>
        <!-- dropdown -->
        <select name="country">
            <option value="korea">한국</option>
            <option value="japan" disabled>일본</option>
            <!-- disabled는 의미가 없음 좀 알면 수정 가능하기 때문 -->
            <option value="china" selected>중국</option>
        </select>
        <input name="number" type="range" min="0" max="100" step="10" value="0">
    </form>
</body>
</html>
```



##### 3.2.9 예제

###### 예제1

```html
<!DOCTYPE html>
<html>
    <head>
        <h1>프로그래밍 교육</h1>
        <a href="#python">파이썬</a>
        <a href="#web">웹</a>
        <a href="index.html">html연습공간</a>
        <hr>
    </head>
    <body>
        <h2 id="python"><a href="https://docs.python.org/ko/3/tutorial/index.html" target="_blank">파이썬</a></h2>
        <h3>Number type</h3>
        <h4>파이썬에서 숫자형은 아래와 같이 있다.</h4>
        <ul>
            <li>1. int</li>
            <li>2. float</li>
            <li>3. complex</li>
            <li><del>4. str</del></li>
        </ul>
        <h3>Sequence</h3>
        파이썬에서 시퀀스는 아래와 같이 있다
        <h4><b>시퀀스는 for문을 돌릴 수 있다!!</b></h4>
        <ul>
            <li>1. str</li>
            <li>2. list</li>
            <li>3. tuple</li>
            <li>4. range</li>
        </ul>
        <hr>
        <h2 id="web"><a href="https://developer.mozilla.org/ko/" target="_blank">웹</a></h2>
        <h3>기초</h3>
        <ul>
            <li style="list-style-type: circle">HTML</li>
            <li style="list-style-type: circle">CSS</li>
        </ul>
    </body>
</html>
```

###### 예제2 - Table 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        table, tr, td{
            border:1px solid darkolivegreen
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <td align="middle" colspan="4">점심메뉴</td>
        </tr>
        <tr>
            <th></th>
            <th>월</th>
            <th>화</th>
            <th>수</th>
        </tr>
        <tr>
            <td>특식</td>
            <td>초밥</td>
            <td>바베큐</td>
            <td>삼겹살</td>
        </tr>
        <tr>
            <td>한식</td>
            <td>육개장</td>
            <td>미역국</td>
            <td>삼계탕</td>
        </tr>
    </table>
</body>
</html>
```

###### 예제3 - 테이블 만들기2

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        table, td, tr{
            border:1px solid darkgoldenrod;
            text-align: center;
            color: royalblue;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>TIME</th>
            <th>INDOOR</th>
            <th colspan="2">OUTDOOR</th>
        </tr>
        <tr>
            <td></td>
            <td>소극장</td>
            <td>잔디마당</td>
            <td>대공연장</td>
        </tr>
        <tr>
            <td>10:00</td>
            <td rowspan="2">안녕하신가영</td>
            <td></td>
            <td>10CM</td>
        </tr>
        <tr>
            <td>13:00</td>
            
            <td rowspan="2">선우정아</td>
            <td rowspan="2">참깨와 솜사탕</td>
        </tr>
        <tr>
            <td>15:00</td>
            <td></td>
        </tr>
        <tr>
            <td>17:00</td>
            <td>크러쉬</td>
            <td></td>
            <td>폴킴</td>
        </tr>
    </table>
</body>
</html>
```

###### 예제4 - 서브웨이 주문서 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <h1>FORM</h1>
</head>
<body>
    <form action="#">
        <P>주문서를 작성하여 주십시오.</P>
        지점명:<input type="text" value="덕명점" readonly> <br>
        이름:<input name="username" type="text" placeholder="이름을 입력해주세요" required autofocus><br>
        날짜:<input name="date" type="date" value="2019-01-13"><br>
        <h3>1. 샌드위치 선택</h3>
        <input type="radio" name="sandwich" value="egg">에그마요<br>
        <input type="radio" name="sandwich" value="bmt">이탈리안 비엠티<br>
        <input type="radio" name="sandwich" value="tba">터키 베이컨 아보카도<br>
        <hr>
        <h3>2. 사이즈 선택</h3>
        <input name="number" type="number" min="15" max="30" step="15" value="15">
        <hr>
        <h3>3. 빵</h3>
        <select name="bread">
            <option value="honey">허니오트</option>
            <option value="flat" disabled>플랫브래드</option>
            <option value="hati">하티 이탈리안</option>
        </select>
        <hr>
        <h3>4. 야채/소스</h3>
        <input type="checkbox" name="vegi" value="tomato">토마토<br>
        <input type="checkbox" name="vegi" value="cucumber">오이<br>
        <input type="checkbox" name="vegi" value="hala">할라피뇨<br>
        <input type="checkbox" name="vegi" value="hot">핫 칠리<br>
        <input type="checkbox" name="vegi" value="barbeque">바베큐<br>
        <br>
        <input type="submit" value="submit">
    </form>
</body>
</html>
```

