# Markdown

[TOC]



## 1. Typora

### [공식 가이드](http://www.markdownguide.org)

### 1.1 Heading

```
# H1입니다.
## H2입니다.
### H3입니다.
#### H4입니다.
##### H5입니다.
```

### 1.2 List

```
* 순서 없는 리스트
* 순서 없는 리스트

1. 순서 있는 리스트1
2. 순서 있는 리스트2
3. 순서 있는 리스트3
```

- 순서 없는 리스트
- 순서 없는 리스트

1. 순서 있는 리스트1

2. 순서 있는 리스트2

3. 순서 있는 리스트3

### 1.3  코드 작성(Code snippet)

```
​```python
print("hello, world")
​```
```

```python
print("hello, world")
```

### 1.4 링크 연결

```
[구글로 가는 링크](https://google.com)
```

[구글로 가는 링크](https://google.com)

### 1.5 글씨 꾸미기

```
*안녕*or_안녕_
**안녕**or__안녕__
***안녕***or*__안녕__*
```

*안녕*

**안녕**

***안녕***

### 1.6 문단 꾸미기

```
---
***
> 안녕하세요?
인용문 공간입니다.
```

------

------

> 안녕하세요?
> 인용문 공간입니다.

### 1.7 기타

ctrl+/ : 화면 변환





## 2. jupyter notebook

### 2.1 기본 설정

#### 2.1.1 설치하기

```powershell
$ pip install jupyter notebook
```

- 설치 끝나면 업데이트 자동으로 하는거 명령어 뜸 그것도 입력

```powershell
$ jupyter notebook
```

- 명령어로 실행
- `ctrl + c` 로 종료

#### 2.1.2 추가 확장

##### 2.1.2.1 nbextensions

> 각종 설정을 할 수 있게 해준다.

```powershell
$ pip install jupyter_contrib_nbextensions
$ jupyter contrib nbextension install --user
```

하면 `jupyter notebook`에 `nbextensions` 탭이 추가됨.

#### 2.1.3 폰트 설정

- D2 font 사용

사용자 > 사용자폴더 > .jupyter > custom폴더 생성 > custom.css파일 생성

```python
.CodeMirror {font-family: D2Coding;}
```

입력 후 저장

서버 재부팅