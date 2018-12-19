# HTML/CSS 기초

사용하기 전에

* 첫줄에 <!Doctype html>이라고 쓴다. 요샌 안해도 되는데 이게 기본
* 3가지 추가기능 설치 
  * HTML snippets
  * HTML CSS Support
  * Auto Close Tag

기본 구조

```html
<!Doctype html>
<html>
    <head>
        <!-- 문서의 정보를 담고 있다. -->
        <title>네이버</title> <!-- 탭에 표시되는 이름 -->
    </head>
    <body>
        <!-- 문서의 내용을 담고있다. 실제로 브라우저에서 보이는 내용들 -->
        <p>
            본문
        </p>
    </body>
</html>
```

CSS

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

