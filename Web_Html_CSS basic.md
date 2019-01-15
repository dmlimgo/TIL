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

#### 2.2 CSS 적용하기

[마소 통계](https://developer.microsoft.com/en-us/microsoft-edge/platform/usage/)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <style>
        h2 {
            color: blueviolet;
        }
    </style>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- 다양한 방법으로 style 적용하기 -->
    <h1 style="color: aquamarine">inline css 적용</h1>
    <h2>내부참조, embedding</h2>
    <h3>외부참조, 파일 link (태그를 기억하자)</h3>
</body>
</html>

style.css
h3 {
    color: wheat;
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <link rel="stylesheet" href="01.css">
</head>
<body>
    <p>20px</p>
    <ol>
        <!-- li : html*1.2 == 20*1.2 -->
        <!-- root에 따라 움직임 -->
        <li>1.2rem</li>
    </ol>
    <ul>
        <!-- ul : 20px*1.2 -->
        <!-- li : ul*1.2 == 20*1.2*1.2 -->
        <!-- 상위요소에 따라 영향을 받음 -->
        <li>1.2em</li>
    </ul>
    <!-- 높이 반응형 -->
    <p class="vh">5vh</p>
    <!-- 넓이 반응형 -->
    <p class="vw">5vw</p>
    <!-- 높이 와 너비 중 최소값에 의해 움직임 -->
    <p class="vmin">10vmin</p>
</body>
</html>

css
html {
    font-size: 20px;
}
ol, ol li {
    font-size: 1.2rem;
}
ul, ul li {
    font-size: 1.2em;
}
.vh {
    font-size: 5vh;
}
.vw {
    font-size: 5vw;
}
.vmin {
    font-size: 10vmin;
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <link rel="stylesheet" href="02.css">
</head>
<body>
    <p>빨간색</p>
    <h1>Tag 선택자</h1>
    <h2 class="pink">클래스 선택자</h2>
    <h3 id="yellowgreen">아이디 선택자</h3>
    <h3 class="pink" id="yellowgreen">id > class</h3>
    <h2 class="pink">class > tag</h2>
    <!-- css를 적용시키기 위해서는 마크업을 하고 선택자를 부여한다. -->
    <!-- span, div태그는 의미는 없지만 css 적용을 위해서 활용한다. -->
    <p><span class="pink">핑크색</span>,
        <span id="yellowgreen">노란색</span></p>
    <p class="bold">볼드체1</p>
    <!-- 두개 class 동시 적용, 여기 순서말고 css에서 순서대로 마지막 것이 적용 됨 -->
    <p class="bold blue pink">볼드체 동시적용</p>
    <p><strong>볼드체2</strong></p>
    <p><b>볼드체3</b></p>
</body>
</html>

02.css
/* 모든 코드에 적용 */
* {
    color: red;
}
h1 {
    color: blue;
}

.pink {
    color: palevioletred;
    /* !important 진짜 중요하다 싶으면 쓴다 */
}
#yellowgreen {
    color: yellowgreen;
}
h2 {
    color: white;
}
/* * < tag < class < id */
.blue {
    color: blue;
}

.bold {
    font-weight: bold;
}
```

2.2.3 selector 심화

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <link rel="stylesheet" href="03.css">
</head>
<body>
    <p>그룹 선택자 적용</p>
    <h3>그룹 선택자 적용</h3>
    <p class="black_bg">그룹</p>
    <p class="white">그룹</p>
    <div class="red">0.3투명 빨강</div>
    <div class="blue">blue</div>
    <div></div>
    <hr>
    <!-- h1+p -->
    <h1>h1</h1>
    <p>h1 형제 p</p>
    <hr>
    <!-- h1~p -->
    <h1>h1</h1>
    <h2>h2</h2>
    <p>h1 형제 p</p>
    <hr>
    <ol id="chocolate">
        <li>ol 자식 li</li>
        <li>드림카카오99%</li>
        <li>쿠앤크</li>
    </ol>
    <div id="chocolate">
        <li>화이트초코</li>
    </div>
    <ul>
        <div>
            <li>ul 자식 li</li>
            <li>둘째자식</li>
            <li>셋째자식</li>
        </div>
    </ul>
    <div class="blue pink white">
        <li>ㅋ</li>
    </div>
</body>
</html>

03.css
/* 그룹 선택자 */
p, h1, h2, h3{
    color: gray;
}
.black_bg, .white {
    color: white;
    background-color: #000000;
}
/* div가 뭘 어떻게 하기 때문에 고정..? */
div {
    width: 100px;
    height: 100px;
    border: 1px solid black;
}
.red {
    background-color: rgba(255, 0, 0, 0.3);
}
.blue {
    background-color: rgb(0, 0, 255);
}
/* html에서 div+div+div 한 것과 같다 */
/* 인접선택자, red 다음 blue 다음 div를 설정한다. */
.red + .blue + div{
    background-color: purple;
}
h1 + p {
    color: goldenrod;
}
/* h1 밑에 있는 형제 */
h1 ~ p {
    color: goldenrod;
}
/* 부모자식 표시 */
ol > li {
    color: darkgreen;
}
#chocolate > li{
    color: chocolate;
}
/* div.blue.white.pink */
/* <div class="blue white pink" */
/* ol 중 id가 chocolate인 것 */
ol#chocolate > li{
    color: chocolate;
}
/* ul 밑에 어디있든지 */
ul  li {
    color: lime;
}
/* 둘째부터 */
ul li+li {
    color: orange;
}
/* nth-child(2) 자식 중에 2번째 */
/* nth-of-type(2) 형제 중에 2번째 */
ul li:nth-of-type(2) {
    color: violet;
}
```

2.2.4 boxmodel

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <link rel="stylesheet" href="04.css">
</head>
<body>
    <!-- 기본적으로 width는 부모의 영향을 받는다. -->
    <!-- div가 body의 50%이므로, p태그 영역도 50% -->
    <div>
        <p>100%</p>
    </div>
    <div style="width: 50%">
        <p>안녕?</p>
    </div>
    <div class="square">
        <p>컨텐츠영역 100*100</p>
    </div>
    <br>
    <div class="square padding-10">
        <p>padding 10 -> 120*120</p>
    </div>
    <br>
    <div class="square padding-10 border-box">
        <p>100*100 (padding 포함)</p>
    </div>
    <!-- 기본적으로 남은 너비는 오른쪽으로 붙는다. -->
    <!-- margin-left: auto는 왼쪽에 남은 너비를 붙인다.(오른쪽 정렬처럼 보임) -->
    <!-- margin: auto는 오른쪽/왼쪽에 반반 나눠준다.(가운데 정렬) -->
    <div class="square margin-50">
        <p>100*100 margin 50</p>
    </div>
    <div class="square margin-top-100">
        <p>100*100 margin top 100</p>
    </div>
    <div class="square margin-50">
        <p>100*100 margin 10</p>
    </div>
    <div class="square" style="margin-left:auto">
        <p>오른쪽 정렬</p>
    </div>
    <div class="square" style="margin:auto">
        <p>가운데 정렬</p>
    </div>
    <div class="square border0">
        <p>border 기본 설정</p>
    </div>
    <div class="circle">
        <p style="margin:auto">1</p>
    </div>
    <div class="football">
        <p>football</p>
    </div>
</body>
</html>

css
.square {
    width: 100px;
    /* 높이는 상속을 받지 않고 컨텐츠만큼 가져간다 */
    height: 100px;
    background-color: skyblue;
}
.padding-10 {
    padding: 10px;
}
.border-box {
    box-sizing: border-box;
}
.margin-50 {
    margin: 50px;
}
/* 위에만 설정 */
.margin-top-100 {
    margin-top: 100px;
    /* right, bottom, left */
    /* 시계방향으로 외우자 */
}
.margin-50 {
    margin: 10px 20px 30px 40px;
}
/* t lr b 3개쓰면 lr이 같이 쓰인다 */
.margin-3 {
    margin: 10px 20px 30px;
}
/* tb lb 이 같이 묶인다 */
/* margin-left: auto는 오른쪽 끝으로 보냄 */
/* margin: auto는 가운데로 보냄 */
.margin-2 {
    margin: 20px 40px;
}
.border0 {
    border-style: dashed;
    border-bottom-style: dotted;
    border-top-style: double;
    border-left-style: outset;
    border-bottom-color: aqua;
    /* 한줄에 border: 2px solid aqua 두께 타입 색상 순서대로 */
}
.circle {
    width: 100px;
    height: 100px;
    border-radius: 100px;
    /* 끝에서 가운데까지를 잘라서 px만큼 원을 만든다. */
    background-color: wheat;
}
.football {
    width: 100px;
    height: 100px;
    background-color: brown;
    border-radius: 15px 75px
}
```

2.2.5 display

```html
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
    <link rel="stylesheet" href="05.css">
</head>
<body>
    <!-- 검사>display요소가 block이냐 inline이냐에 따라 다름 -->
    <h1>block</h1>
    <p>block</p>
    <div>block</div>
    인라인 : <input type="text">
    <span>인라인</span>
    <a href="https://google.com">인라인</a>
    <h2>안녕하세요</h2>
    <h2>이재찬입니다.</h2>
</body>
</html>

css
h2 {
    display: none;
}
```

* 안보이게 하기

> style에서 display:none ->공간을 없앰

> ​		visablity:hidden-> 안보이게만 함

* static위치: 기본적으로 부모위치를 기준으로 함
* relative(상대위치):

3.2.9 예제 - 사각형 갖고 놀기

```html
<!DOCTYPE html>
<html>
<head>
  <title>BOX</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green">
      <div class="small-box" id="purple"></div>
    </div>
    <div class="small-box" id="blue">
      <div class="small-box" id="orange"></div>
    </div>
    <div class="small-box" id="pink"></div>
  </div>
  <!-- relative : position 적용 전(static일 때) 자기 자신이 원래 있었던 위치 -->
  <!-- (우측 하단을 보자) -->
  <!-- 움직이고 원래 있었떤 공간이 유지됨 -->
  <!-- absolute : 가장 가까운 조상 중에 static이 아닌 것의 위치 -->
</body>
</html>

css
.big-box {
    position: relative;
    margin: 100px auto 500px;
    border: 5px solid black;
    width: 500px;
    height: 500px;
  }

  .small-box {
    width: 100px;
    height: 100px;
  }
  
  #red {
    position: relative;
    background-color: red;
    left: 400px;
    /* relative일때는 bottom: 0; 은 못 씀 */
    top: 400px;
  }
    
  #gold {
    position: fixed;
    background-color: gold;
    right: 0;
    bottom: 0;
  }

  #green {
    position: relative;
    background-color: green;
    left: 200px;
    top: 100px;
  }

  #blue {
    background-color: blue;
    position: relative;
    top: -100px;
    left: 100px;
  }

  #pink {
    position: relative;
    background-color: pink;
    left: 0;
    bottom: 300px;
  }

  
  
  /*  심화 */
  #purple {
    position: relative;
    background-color: purple;
    left: 100px;
    top: 100px;
  }
  
  #orange {
    position: relative;
    background-color: orange;
    left: 100px;
    top: -100px;
  }
```





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

