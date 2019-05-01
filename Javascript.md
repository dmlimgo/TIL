## Javascript

> 190430 강의내용

배경 : script를 돌리기 위한 표준들이 브라우저마다 달랐고 그 표준(ES1, ES2, ..., ES2017)들이 뭉쳐져서 여기까지 왔다.

자바스크립트의 함수는 일급 객체이다.

==일급 객체의 조건==

1. 변수나 특정한 오브젝트에(배열) 함수를 저장할 수 있다.
2. 함수의 인자로 전달할 수가 있어야 한다.
3. 함수 자체를 return 할 수 있어야 한다.
4. 이름과 상관없이 구별이 가능하다. (익명으로 표현 가능)
5. 동적으로 속성값(property) 할당이 가능하다.

### 0. 환경설정

- 구글 크롬의 Console창과 VS Code에서 실습을 진행한다.

- ==VS Code==의 경우 *open in broswer*를 설치해두면 단축키로 브라우저를 열 수 있다.

- *JavaScript (ES6) code snippets*도 혹시모르니 설치해둔다.



![js1](image\js1.PNG)



### 1. Commands

* `script`태그는 대체로 `body`의 닫는 태그 위에 쓴다.

* 이 문서에서는`script`태그는 생략한다.

* console창에서 밑의 줄로 이동해서 입력하려면 shift-enter를 사용하면 된다.

  ```JS
  <body>
      ...
      <script>
      </script>    
  </body>
  ```

* 주석처리는 다음과 같이 한다.

  ```JS
  //
  /* */
  ```

#### 1.1 document, window

> 웹 문서 자체를 조작하는 메소드들을 가지고 있다.

##### 1.1.1 window.innerwidth

> 현재 창의 너비를 출력한다

##### 1.1.2 window.print()

> 현재 창을 인쇄(출력)한다.

##### 1.1.3 document.title

```js
> document.title = '에듀싸피'
// 문서의 제목을 '에듀싸피'로 변경
```

```js
> document.title
'에듀싸피'
```

##### 1.1.4 document.write()

```js
> document.write('SSAFY 짱!')
// 문서에 'SSAFY 짱!' 을 출력한다.
> document.write('<h1> SSAFY 짱! </h1>')
// 태그도 사용 가능하다.
```



### 1.2 ~

#### 1.1 alert

> 팝업메세지를 띄워준다.

```javascript
alert('자바스크립트, 안녕!')
```

#### 1.2 console.log

> 디버깅을 위한 코드. Console창에 해당 메세지를 띄워준다.

```javascript
console.log('안녕?')
```

#### 1.4 document.write

> 문서에 글자를 쓴다.

```js
document.write('<h1>SSAFY 최고</h1>')
```

#### 1.5 document.querySelector

![js2](image\js2.PNG)

#### 1.6 var <i>varname</i>

변수가 글로벌인지 아닌지에 대한 것은 반드시 선언을 해줘야 한다.

```js
// 변수 hoisting
// 자바스크립트에서 모든 선언과 관련된 (변수, 함수 등) 문장은 호이스팅 된다.
// 변수는 1)선언단계 2)초기화 단계 3)할당 단계를 거치게 된다.
console.log(name) // undefined
var name='슬기'
console.log(phoneNumber) // phoneNumber is not defined error.
---------------------
슬기
```

단점 변수를 새로 선언해줘도 오류가 발생하지 않는다. (오류가 발생했으면 좋겠다는 것이 대다수 사용자들의 생각) > let 키워드를 사용하여 해결

```js
var d = 6
var d = 9
```



#### 1.7 let, const 키워드 (ES6+ 에서 등장)

var의 단점을 개선해 새로 등장

let은 변수에 const는 상수에 쓴다.

```js
let e = 100
let e = 20
Uncaught TypeError: Assignment to constant variable.
```

```js
let e = 211
e = 30
```



var와 let의 차이

```js
for (var i = 0; i < 3; i++){
	console.log(i)
}
console.log('=====================')
console.log(i) //i 값이 증가한 채로 존재함
-----------------------------------------
0
1
2
==================
3
```

```js
for (let i = 0; i < 3; i++){
	console.log(i)
}
console.log('=====================')
console.log(i) //i 값이 없음
-----------------------------------------
0
1
2
==================
Uncaught ReferenceError: i is not defined at ~
```

var는 for문 이후에도 사용 가능, let은 불가능



#### 1.8 변수 합치기

```js
const firstname = 'happy'
const lastname = 'hacking'
const name = firstname + lastname
document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)ㄴ
// '가 아닌 `임에 주의하자
document.write(`<h1>${name}</h1>`)
```



#### 1.9 prompt

> 변수 입력받기

```js
let username = prompt('너 누구냐?')
let message = `<h1>${username}</h1>`
document.write(message)
```



#### 1.10 if 조건문

```js
let username = prompt('너 누구냐?')
let message

// 자바스크립트에서는 ===이 파이썬의 ==과 같은 비교 연산자이다.
// ===(!==) : 일치함을 비교(값, 타입)
// ==(!=) : 동등함을 비교(값), 타입이 암묵적 변환될 수 있음.
// 123 == '123' : true
if (username === '태현'){
    message = `<h1>안자?</h1>`
} else if (username === '슬기'){
    message = `<h1>${username}는 일하자</h1>`
} else {
    message = `<h1>${username}은 수업듣자</h1>`
}
document.write(message)
```



#### 1.11 while 

```js
// while
let i = 0
while (i < 10) {
    console.log(i)
    i++
}
-----------------
0
1
2
...
8
9
```



#### 1.12 for

```js
let myArray = [1, 2, 3]
for (let k = 0; k < 3; k++){
    console.log(myArray[k])
}
// 혹은
for (let k of myArray) {
    console.log(k)
}
```



#### 1.13 array

```js
let numbers = [1, 2, 3, 4]
```

###### 1.13.1 

```js
> numbers.length
4
> numbers.reverse()
[4, 3, 2, 1]
> numbers[0]
1
> numbers[-1]
Error
> numbers.push('push') // 길이와 값을 리턴
  numbers
(5) [1, 2, 3, 4, "push"]
> numbers.pop()
// 범위 밖이면 제일 마지막거 뽑는다.
4
```

```js
> numbers.include(1)
true
> numbers.join('-')
"1-2-3"
> numbers.indexOf(1)
0
> numbers.indexOf(9) //없는 값
-1
> numbers.shift() // 앞의 값을 뺌
1
> numbers.unshift(1) // 길이를 리턴
2
```

```js
> numbers.sort()
[1, 1, 2, 3]
> numbers.slice(0, 2)
(2) [1, 1]
> numbers.slice(-2) // 음수는 인덱스는 안되고 슬라이스는 됌
(2) [2, 3]
```



#### 1.14 dict

자바스크립트의 데이터 타입에는 - 원시타입이 있고 오브젝트 타입이 있는데

원시 타입에는 아래와 같은 것들이 있다.

Boolean(true, false), null, undefined, number, string

```js
// 자바스크립트 object 표기법
let seulgi = {
    name: 'seulgi',
    age: 26,
    number: '010-1111-2222'
}
```

```js
> typeof seulgi
"object"
> typeof [1, 23, 4]
"object"
> typeof 1
"number"
```

```js
// ES6+
// 변수를 그대로 넣으면 변수명: 값
let name = 'taehyun'
let stuffs = ['공기청정기', '커피머신']
let taehyun = {
    name,
    stuffs
}
let jsonData = JSON.stringify(taehyun)
```

```js
> jsonData
"{"name":"taehyun","stuffs":["공기청정기","커피머신"]}"
```

```js
let jsonParse = JSON.parse(jsonData)
```

```js
> jsonParse
{name: "taehyun", stuffs: Array(2)}
```



#### 1.15 function

```js
//1. 함수 선언식
function add(num1, num2) {
    return num1 + num2
}
console.log(add(1, 3))
----------------------------
4
//2. 함수 표현식
//함수 자체를 변수로 저장해서 씀(1급개체)
let add2 = function add3(num1, num2){
    return num1 + num2
}
console.log(add2(1, 3))
//console.log(add3(1, 3)) 오류
----------------------------
4
// 3. ES6+ Arrow Function
let sub = (num1, num2) => {
    return num1 - num2
}
// 3-1. 인자가 하나인 경우, () 생략가능
//		단순 리턴인 경우(리턴이 한줄에 딱 끝나는 경우), {} 및 리턴 키워드 생략 가능
let greeting = name => `${name}, 안녕!`
let mul = (num1, num2) => num1 * num2
console.greeting('동명')
console.log(mul(1, 4))
-----------------------------
"동명, 안녕!"
4
// 3-2. 인자가 없는 경우에는 () 작성
let hello = () => 'hello, world!'
// object 리턴 시 반드시 () 묶어서 작성
let me = (name, age) => ({name, age})
sonsole.log(me('hi', 3))
// 익명함수 만들어 즉시 실행
((a, b) => a * b)(4, 5)
```

실습 Arrow Function으로 바꿔보기

```python
def negative(num):
    return -1 * num
def gutenTag():
    return 'Guten Tag'
def veitnam(member):
    member_base = '황여진'
    return f'{member_base}'
```

```js
let veitnam = (member) => {
    member_base = '황여진'
    console.log(member)
    console.log(member_base)
    return `${member_base}와 ${member}가 베트남에 가요`
}
console.log(veitnam('누군가'))
```

```js
// 만약, default args (기본인자)
let bonjour = (name='동명') => `${name}, bonjour`
```

```js
// 4. 익명 함수
(function(num) {return num*num}) // 자바스크립트가 알아서 ;를 하기 때문에 괄호를 씌운다.
```

```js
// 5. 즉시 실행 함수 (익명함수 + 호출) - IIFE(Immediately Invoked Function Expression)
(function(num) {return num*num})(5)
```



```js
// 배열을 다 받아서 다 더해주는 함수를 작성 해주세요.
// numberAddEach(numbers)
const numberAddEach = (numbers) => {
    let hap = 0
    for (let i = 0; i < numbers.length; i++){
        hap += numbers[i]
    }
    return hap
}
console.log(numberAddEach([1, 2, 3, 4, 5, 10000]))
```

```js
const numberEach = (numbers, oper) => {
    let result
    for (const number of numbers){
        result = oper(number, result)
    }
    return result
}

const AddEach = (number, result = 0) => result + number
const SubEach = (number, result = 0) => result - number
const MulEach = (number, result = 1) => result * number
const DivEach = (number, result = 1) => result / number

// 롤백
console.log(numberEach([1,2,3], AddEach))
console.log(numberEach([1,2,3], SubEach))
console.log(numberEach([1,2,3], MulEach))
console.log(numberEach([1,2,3], DivEach))
```

```js
// 이것저것 콜백에 익명함수에 뭐 다 합쳐진 최종본. 이게 눈에 들어오도록 공부하자
console.log(numberEach([10, 20, 30], (number, result=0) => result + number))
console.log(numberEach([10, 20, 30], function(number, result=0){
    return result + number
}))
```

```js
// 또다른 예시, 콜백으로 구성되어 있다.
let foods = ['빠삐코', '메로나', '돼지바']
foods.forEach(function(element, idx, foods) {
    console.log(element, idx, foods)
})
```

#### 1.Example

```js
const avengers = ['닥터스트레인지', '토르', '헐크', '아이언맨', '스파이더맨', '그루트', '너구리', '앤트맨']
avengers.forEach( hero => console.log(hero) )
avengers.forEach( function (hero){console.log(hero)})
// 2. map
const numbers = [1, 2, 3]
const strNumbers = numbers.map(number => String(number))
console.log(strNumbers)
const squareNumbers = numbers.map(number => number*number)
console.log(squareNumbers)
const squareNumbers2 = numbers.map(function(number){return number*number})
console.log(squareNumbers2)
const seulgi = [
    {'velocity': 40, 'time': 50},
    {'velocity': 100, 'time': 60},
    {'velocity': 20, 'time': 1000},
]
const distances = seulgi.map(function(obj){
    return obj.velocity * obj.time
})
console.log(distances)
const distances2 = seulgi.map(obj => obj.velocity * obj.time)
console.log(distances2)
```

하나 더 있음 정리해야함!!