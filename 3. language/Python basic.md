# Python basic

[TOC]

---



## 0. 가이드 라인

#### 1) [Python tutorial](https://docs.python.org/3/tutorial/index.html)

#### 2) [Python Style Guide (PEP-8)](https://www.python.org/dev/peps/pep-0008/)

* 파이썬에서 장려하는 스타일 가이드. indentation(들여쓰기)와 같은 내용이 들어있음. 가독성을 높이기 위해 알아야 함.



## 1. 기본 단축키

`ctrl+/` : 주석 처리하기



## 2. 문자열 조작

### 1) 기본 출력 방식

```python
# 기본 방법
print("안녕하세요")
print("저는 이몽명입니다.")
print("만나서 반갑습니다.")

# 다른 방법
print("""안녕하세요
	저는 이몽명입니다.
	만나서 반갑습니다.
	""")
```

```python
#여러줄 출력은 \를 이용한다.
print('\
안녕')
```



### 2) 문자열 안에 변수 출력하기 (String interpolation)

#### 		(1) F-String

```python
name = "홍길동"
 print(f"안녕하세요, {name}입니다.")
 #=> "안녕하세요, 홍길동입니다."
```

#### 	(2) [Pyformat](https://pyformat.info/)

```python
name = "홍길동"
english_name = "hong"
print("안녕하세요, {}입니다. My name is {}".format(name,english_name))
#=> "안녕하세요, 홍길동입니다. My name is hong"

# 괄호 안의 숫자에 따른 변화도 알아두자
print("안녕하세요, {1}입니다. My name is {0}".format(name,english_name))
#=> "안녕하세요, hong입니다. My name is 홍길동"
print("안녕하세요, {1}입니다. My name is {1}".format(name,english_name))
#=> "안녕하세요, hong입니다. My name is hong"
```

#### 		(3) 모르면 이렇게 하자

```python
name = "홍길동"
print("안녕하세요. " + name + "입니다.")
```

### 3) 함수





## 3. 자료형

### 1) List

`list` 는 배열 또는 array라고도 불린다. 

인덱스를 통해 값에 접근할 수 있다.

```python
menu = ["중국집","까르보나라","된장탕","떡볶이"]
menu[0]
#=> 중국집
```

### 2) Dictionary

* `Dictionary`는 hash(해시)라고도 불린다. `key`와 `value`가 짝지어져 있다.
* `key`에는 `list`나 `dictionary`형태 빼고는 다 된다.

#### (1) 기본 형식

```python
# 기본 형식
phonebook = {
    "중국집":"561221",
    "초밥집":"123",
    "한식집":"118"
}
# 다른 형식으로도 표현 가능
phonebook2 = dict(중국집=1, 초밥집=2)

# 변수 추가
phonebook["분식집"]="123124"

# dictionary 안의 dictionary
idol = {
    "소녀시대" : dict(윤아 = 29, 태연 = 30),
    "샤이니" : dict(태민 = 28, 키 = 29)
}
```

#### (2) 특징

- `for` 문에 넣어서 출력하면 `key` 만 출력된다

```python
for what in phonebook:
    print(what)
    print(phonebook[what])
```

​	`key`가 있으면 `value`도 출력가능하지만

​	`value`만 있으면 `key`를 출력할 수 없기 때문이다.

- 한 줄에 출력을 하고 싶다면

```python
for what in phonebook:
    print(what, end=' ')
    print(phonebook[key])
```

​	마지막 문자를 띄어쓰기로 바꿔주면 엔터가 출력되지 않는다. 혹은

```python
for key, value in phonebook.items():
    print(key, value)
```

​	이것만 알고 있어도 활용이 가능

- `key`나 `value`만 출력하고 싶다면

```python
for key in phonebook.keys():
    print(key)
```

```python
for value in phonebook.values():
    print(value)
```

- 이 요소가 리스트 안에 있니?

```python
a = [1,2,3]
4 in a
False
3 in a
True

b = "asdf"
"f" in b
True
"z" in b
False
```

```python
len(dic) # dictionary의 갯수
```

```python
dir(score.values()) # 사용가능한 함수 목록
```

```python
min(a)
max(b)
#리스트의 최대, 최소 구하기
```



#### (3) 예제

```python
"""
파이썬 dictionary 활용 기초!
"""
# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답
print("=====Q1=====")
# 내 풀이
for x in iu_score.values():
    sum = sum + x
avg = sum/len(iu_score)
print(avg)
# 강사님 풀이
avg = sum(iu_score.values())/len(iu_score)
print(avg)

# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답
print("=====Q2=====")
# 내 풀이
for key in score:
    total_score = 0
    for value in score[key].values():
        total_score += value
    avg = total_score/len(score[key])
    print(f"{key}의 평균 {avg}")
# 강사님 풀이
total_score = 0
length = 0
for person_score in score.values():
    for inidividual_score in person_score.values():
        total_score += inidividual_score
        length +=1
average_score = total_score / length
print(average_score)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
# 내 풀이
for key in city:
    total_score = 0
    avg = 0
    for value in city[key]:
        total_score += value
    avg = total_score/len(city[key])
    print(f"{key}의 평균 {avg:0.2f}")
# 강사님 코드
for name, temp in city.items():
    # 첫번째 시행때
    # name = "서울"
    # temp = [-6, -10, 5]
    average_temp = sum(temp)/len(temp)
    print(f"{name} : {average_temp}")
# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
min = 99
max = -99
min_city = ""
max_city = ""
for key in city:
    total_score = 0
    avg = 0
    for value in city[key]:
        total_score = total_score + value
    avg = total_score/len(city[key])
    if avg < min:
        min = avg
        min_city=key
    elif avg > max:
        max = avg
        max_city=key
print(f"가장 추운 곳 {min_city} : {min:0.2f}")
print(f"가장 더운 곳 {max_city} : {max:0.2f}")

min = 99
max = -99
min_city = ""
max_city = ""
for key in city:
    total_score = 0
    avg = 0
    for value in city[key]:
        if value < min:
            min = value
            min_city=key
        elif value > max:
            max = value
            max_city=key
print(f"가장 추운 곳 {min_city} : {min}")
print(f"가장 더운 곳 {max_city} : {max}")

'''위에랑 충돌남
# 강사님 풀이
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
	}

cold = 0
hot = 0
cnt = 0
hot_city = ""
cold_city = ""
for name, temp in city.items():
    # 첫 번째 시행 때,
    # name = "서울"
    # temp = [-6, -10, 5]
    if cnt == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        elif max(temp) > hot:
            hot = max(temp)
            hot_city = name
    cnt += 1
print(hot_city)
print(cold_city)
        # 최고 온도가 hot보다 더 더우면, hot에 넣는다.
'''

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
if 2 in city["서울"]:
    print("네")
else:
    print("아니영")

count = len(city["서울"])
correct = 0
for i in range(count):
    if city["서울"][i] == 2:
        correct = 1
if correct == 1:
    print("네 있습니다.")
else:
    print("아뇨 없습니다.")
```

### 3) set (집합)

* 중복된 값을 허락하지 않는 특성이 있다.

```python
a = {1,2,2}
set(a)
=> {1,2}
```

* `&` : 교집합, `-` : 차집합, `|` : 합집합



## 4. 함수

### 1) range

`range` 는 숫자의 범위를 가지고 있다.

`range`가 `list`보다 메모리 효율이 좋다

```python
print(range(5))
#=> range(0,4)

# list 형변환
a = list(range(5))
print(a)
#=> [0,1,2,3,4]

# 반복문 활용
for i in range(3):
    print(i)
#=> 0
#=> 1
#=> 2    
```



### 2) 정렬함수

#### (1) sorted(_)

```python
a = [3,1,2]
sorted(a)
#=> [1,2,3] 
# 정렬된 리스트를 리턴함
print(a)
#=> [3,1,2]
a = sorted(a)
print(a)
#=> [1,2,3]
```

#### 	(2) .sort()

```python
a = [3,1,2]
a.sort()
#=> None 
# 'None'을 리턴함
print(a)
#[1,2,3]
```

#### (3) .reverse()

#### (4) reversed(리스트)

### 3) 랜덤함수 

`import random` : 랜덤 함수 사용 명령어

`random.choice(리스트)` : 한개 추출

`random.sample(리스트,갯수)` : 비복원 갯수 추출



### 4) 파일 입출력 함수

#### (1) 기본 함수

```python
변수 = open("파일명", "옵션")			# 파일을 열어 리턴함.
with open("파일명", "옵션") as 변수:	 # 이 방식을 선호
```

* 옵션 - `w` 덮어쓰기, `r` 읽기, `a` 이어쓰기
* `python`에서 `with`는 `context manager`라고 부른다. with 블록 내에서 파일을 조작하고, 블록이 끝나게 되면 파일이 닫힌다.

```python
변수.write("글 입력")
```

```python
변수.read()	# 글 읽어들여 str로 리턴
```

```python
변수.readline()	# 글 읽어들여 str로 리턴
```

```python
변수.readlines()	# 글 읽어들여 list로 리턴
```

```python
변수.close()
```

#### (2) 예제

##### 	예제 - 파일 읽기

```python
with open("new1.txt", "r") as f:
    line = f.read()
print(line)
```

##### 	예제 - 파일 여러줄 쓰기

```python
with open("new2.txt", "w") as f:
    for line in range(50):
        f.write(f"{line}번째 줄 입니다.\n")
```

##### 	예제 - 파일 여러줄 읽기

```python
with open("new2.txt", "r") as f:
    '''
    while True:
    	line = f.readline()
    	if line=='':
    		break
    	print(line)
    '''
    # 아래 방식을 쓸 것
    lines = f.readlines()
    for i in lines:
        print(i.strip('\n'))
    # 사실은 lines도 필요없다. open하면서 줄 단위로 불러오기 때문
    for i in f:
        print(i.strip('\n'))
```

* `line = f"{i}{j}={i*j}\n"` 의 형식도 가능

  ##### 예제 - 구구단 출력

```python
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")
```

##### 	예제 - 파일 읽어서 역순으로 다른 파일에 저장

```python
with open("ssafy.txt","w") as f:
    f.write(f"안\n")
    f.write(f"녕\n")
    f.write(f"하\n")
    f.write(f"세\n")
    f.write(f"요\n")
    f.write(f"배\n")
    f.write(f"가\n")
    f.write(f"고\n")
    f.write(f"파\n")
    f.write(f"요\n")

with open("ssafy.txt","r") as f:
    lines = f.readlines()
    lines.reverse() # 사용법에 유의, b=reversed(lines)도 가능
    print(lines)
    
    with open("result.txt","w") as g:
        for i in lines:
            print(i.strip('\n'))
            g.write(i)
```



### 5) 문자열 함수

```python
문자열.strip(문자)	 # 문자열에서 괄호 안의 문자 제거
```

```python
문자열.lstrip(문자) 	 # 문자열의 왼쪽 부분에서 괄호 안의 문자 제거
```

```python
문자열.split("문자")	 # 문자열을 "문자"기준으로 분리해서 리스트로 만듬
```



### 6) map 함수 (알아두자)

```python
map(함수, 반복 가능한 자료형)
# 자료형의 자료에 대해 함수를 모두 실행한 후 결과를 리턴
```





## 5. 모듈

### 1) Os module

#### (1) 사용하기 위한 준비

```python
import os	# os모듈, 운영체제와 관련된 작업을 하는 모듈
```



#### (2) 명령어 모음

[공식 사이트](https://docs.python.org/3/library/os.html)

* ##### 현재 작업중인 폴더를 보여줌

```python
os.getcwd()
```

* ##### 폴더 내의 목록 출력

```python
os.listdir()
```

* ##### 폴더 접근 

```python
os.chdir(r'폴더명')	# r은 절대경로 접근
```

* ##### 파일명 변경

```python
os.rename('현재파일명','바꿀파일명')
os.rename('현재파일명','현재파일명'.replace("문자열","문자열"))
```

##### 

#### (3) 예제

##### 	예제 - 폴더 접근해서 파일명 바꾸기

```python
import os
# SSAFY_지원자 폴더 접근
os.chdir(r'SSAFY_지원자')
# SSAFY지원자 폴더 접근
os.chdir(r'SSAFY지원자')
# 내용 모두 출력
lists = os.listdir()
for x in lists:
    os.rename(x,x.replace("SAMSUNG지원자","SSAFY지원자_"))
```



## 8. 예제

### 1) Day4 (18.12.20) 예제

```python
#문제 1.
#문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

str = input('문자를 입력하세요: ')
# 내 풀이
print(f"{str[0]}{str[len(str)-1]}")
# 강사님 풀이
print(f"{str[0]}{str[-1]}")


#문제 2.
#자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input('숫자를 입력하세요: '))

for num in range(n):
    print(num+1)


#문제 3.
#숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

number = int(input('숫자를 입력하세요: '))

if number % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
# 1이나 0이라면 True나 False이므로 다음과 같이 가능
if number % 2:
    print("홀수 입니다.")
else:
    print("짝수 입니다.")

# 문제 4.
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 국어는 90점 이상,
# 영어는 80점 초과,
# 수학은 85점 초과, 
# 과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
# 다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

if (a >= 90) & (b > 80) & (c > 85) & (d >=80):
    print("퇴근하세요")
else:
    print("야근하세요")

# 문제 5.
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000

prices = input('물품 가격을 입력하세요: ')
price=prices.split(";")
# num_price=map(int, price) 으로하면 간단하게 됨.
num_price=[]

for x in price:
    num_price.append(int(x))

sorted_price=sorted(num_price)
sorted_price.reverse()
print(sorted_price)
```

예제 (로또 몇번만에 당첨될까?)

```python
# 1. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837
# 위의 주소로 요청을 보낸다.
import requests
import random
#camelcase w #snakecase _

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
response = requests.get(url).json() # 바로 변환 가능

# 2. 응답된 결과를 json으로 바꿔서 dictionary처럼 활용한다.

win_nums=[]
for x in range(6):
    win_nums.append(response[f"drwtNo{x+1}"])

bonus_num = response["bnusNo"]
print(f"{win_nums}{bonus_num}")
# 3. 랜덤으로 로또 번호 하나를 추출한다.
# my_nums = random.sample(range(1,46),6)

# 4. 몇 등인지 알아본다.
'''
cnt=0
bns=0
for win_num in win_nums:
    for my_num in my_nums:
        if win_num == my_num:
            cnt += 1
        if bonus_num == my_num:
            bns = 1
print(cnt)
print(bns)

# 5. 등수를 출력한다. 
if bns == 1 and cnt == 5:
    print("2등 입니다.")
elif cnt == 6:
    print("1등 입니다.")
else:
    print(f"{5-cnt+3}등 입니다.")
'''
'''
# 6. 반복
try_count = 0
win_count = 0
while(win_count == 0):
    my_nums = random.sample(range(1,46),6)
    cnt=0
    bns=0
    try_count += 1
    for win_num in win_nums:
        for my_num in my_nums:
            if win_num == my_num:
                cnt += 1
            if bonus_num == my_num:
                bns = 1
    if cnt == 6:
        win_count = 1
    print(try_count, end='\r')
print(f"{try_count}번 만에 당첨!")     
'''
# 강사님 풀이
lucky = [0, 0, 0, 0, 0]
money = 0
for i in range(10000000):
    my_nums = random.sample(range(1,46),6)
    matched = len(set(win_nums) & set(my_nums))

    if matched == 6:
        lucky[0] += 1
        print(i)
        print(3100000000*lucky[0] + 
                 6000000*lucky[1] + 
                 1500000*lucky[2] + 
                   50000*lucky[3] + 
                    5000*lucky[4])
        break
    elif matched == 5 and bonus_num in my_nums:
        lucky[1] += 1
    elif matched == 5:
        lucky[2] += 1
    elif matched == 4:
        lucky[3] += 1
    elif matched == 3:
        lucky[4] += 1
    print(lucky, i, end='\r')
```

짝수 홀수 저장

```python
# 1~100까지 숫자를
# even이라는 list를 만들어서 짝수만 저장
# odd라는 list를 만들어서 홀수만 저장
```

```python
hundred = range(1,101)
even=[]
odd=[]
for x in hundred:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(list(hundred))
print(even)
print(odd)
```



### 2) Day5 (18.12.21) 예제

```python
'''
난이도* 1. 지역(location)은 몇개 있나요?
출력예시)
4
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
false
난이도** 3. dj1반의 반장의 이름을 출력하세요.
출력예시)
박성민
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
난이도*** 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.
출력 예시)
junho
pro2
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 고병석
'''
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "dj1":  {
            "lecturer": "tak",
            "manager": "pro1",
            "class president": "박성민",
            "groups": {
                "1조": ["강신욱", "윤영우", "이민교", "유창오", "황여진", "김민경"],
                "2조": ["노승만", "이재찬", "이주호", "김예지", "유지원"],
                "3조": ["이민지", "김희윤", "박성민", "조인정", "김슬기", "고병석"],
                "4조": ["임동명", "김승훈", "정상영", "정태현", "한단비", "김동민"]
            }
        },
        "dj2": {
            "lecturer": "junho",
            "manager": "pro2"
        }
    }
}
```

`fstring`사용시 " "를 겹쳐서 사용하면 `syntex`오류가 날 수 있다. ' '와 혼용하도록 하자.

```python
print(f"오늘의 당번은 {random.choice(ssafy["classes"])}")
SyntaxError
print(f'오늘의 당번은 {random.choice(ssafy["classes"])}')
```

풀이

```python
# 1번 문제
print(len(ssafy["location"]))

# 2번 문제
print("requests" in ssafy["language"]["python"]["python standard library"])

# 3번 문제
print(ssafy["classes"]["dj1"]["class president"])

# 4번 문제
for key in ssafy["language"].keys():
    print(key)

# 5번 문제
for value in ssafy["classes"]["dj2"].values():
    print(value)

# 6번 문제
for key, value in ssafy["language"]["python"]["frameworks"].items():
    print(f"{key}는 {value}이다.")

# 7번 문제
a = random.choice(ssafy["classes"]["dj1"]["groups"]["3조"])
print(f"오늘의 당번은 {a}")
print(type(a))
print(f'오늘의 당번은 {random.choice(ssafy["classes"]["dj1"]["groups"]["3조"])}')
```

### 3) W3D1 (2019.01.02)

####  





## 9. 기타

-5~256의 값은 메모리에서 쉽게 가져올 수 있도록 주소가 지정되어 있다.

```python
a = [3,1,2]
b = 3
c = [1,2]
print(f"a의 '3'주소 {id(a[0])}")
print(f"b의 '3'주소 {id(b)}")
print(f"a의 '1'주소 {id(a[1])}")
print(f"c의 '1'주소 {id(c[0])}")
```

```python
a의 '3'주소 1456040768
b의 '3'주소 1456040768
a의 '1'주소 1456040704
c의 '1'주소 1456040704                                                   
```

