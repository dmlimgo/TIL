# Javascript

> 190430 강의내용

[TOC]

배경 : script를 돌리기 위한 표준들이 브라우저마다 달랐고 그 표준(ES1, ES2, ..., ES2017)들이 뭉쳐져서 여기까지 왔다.

자바스크립트의 함수는 일급 객체이다.

==일급 객체의 조건==

1. 변수나 특정한 오브젝트에(배열) 함수를 저장할 수 있다.
2. 함수의 인자로 전달할 수가 있어야 한다.
3. 함수 자체를 return 할 수 있어야 한다.
4. 이름과 상관없이 구별이 가능하다. (익명으로 표현 가능)
5. 동적으로 속성값(property) 할당이 가능하다.



## 환경설정

- 구글 크롬의 Console창과 VS Code에서 실습을 진행한다.

- ==VS Code==의 경우 *open in broswer*를 설치해두면 단축키로 브라우저를 열 수 있다.

- *JavaScript (ES6) code snippets*도 혹시모르니 설치해둔다.



![js1](image\js1.PNG)



## 1. Commands

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



#### window.innerwidth

> 현재 창의 너비를 출력한다



#### window.print()

> 현재 창을 인쇄(출력)한다.



#### document.title

> 현재 문서의 제목에 접근한다.

```js
> document.title = '에듀싸피'
// 문서의 제목을 '에듀싸피'로 변경
```

```js
> document.title
'에듀싸피'
```



#### document.write()

> 현재 문서에 출력한다.

```js
> document.write('SSAFY 짱!')
// 문서에 'SSAFY 짱!' 을 출력한다.
> document.write('<h1> SSAFY 짱! </h1>')
// 태그도 사용 가능하다.
```



#### document.querySelector('*query*')

> 가창 처음에 있는 *query*를 선택해서 반환, 없으면 null 반환

![js2](image\js2.PNG)



#### alert

> 팝업메세지를 띄워준다.

```javascript
alert('자바스크립트, 안녕!')
```



#### console.log

> 디버깅을 위한 코드. Console창에 해당 메세지를 띄워준다.

```javascript
console.log('안녕?')
```





## 2. Variable

- 변수가 글로벌인지 아닌지에 대한 것은 반드시 선언을 해줘야 한다.

- 자바스크립트의 데이터 타입에는 - 원시타입이 있고 오브젝트 타입이 있는데

  원시 타입에는 아래와 같은 것들이 있다.

  Boolean(true, false), null, undefined, number, string

#### var <i>varname</i>

> ES6이전에 사용하던 변수 키워드. hoisting으로 어디에 선언되어있던 실행 가능하다.

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
var d = 9 // 문제 없음
```

가장 전역에 선언되어 window에서 인식 가능하다. (let, const는 불가)

```JS
var a = 1
window.a //1
```



#### let, const 키워드 (ES6+ 에서 등장)

> var의 단점을 개선해 새로 등장
>
> let은 변수에 const는 상수에 쓴다.

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

var는 for문 이후에도 사용 가능, let은 불가능

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

let, const는 전역으로 선언되지 않아 window에서 읽을 수 없다.

```js
let a = 1
window.a //undefined
```





#### 변수 합치기 (String)

```js
const firstname = 'happy'
const lastname = 'hacking'
const name = firstname + lastname
document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)ㄴ
// '가 아닌 `임에 주의하자
document.write(`<h1>${name}</h1>`)
```



#### prompt(변수 입력받기)

```js
let username = prompt('너 누구냐?')
let message = `<h1>${username}</h1>`
document.write(message)
```





## 3. if, while, for

#### if 조건문

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



#### while 조건문

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



#### for 반복문

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





## 4. Array (Object)

#### 선언

```js
let numbers = [1, 2, 3, 4]
```



#### *arr*.length

> 배열의 길이



#### *arr*.reverse()

> 배열을 뒤집고 리턴, python과 다르게 변수에 받아두지 않아도 된다.

```js
numbers.reverse() //[4, 3, 2, 1]
```



#### *arr*[] (원소 접근)

```js
numbers //[4, 3, 2, 1]
numbers[0] //4
numbers[-1] //Error (정확한 양의 정수 index만 가능)
```



#### *arr*.push(*val*)

> 배열의 마지막에 요소를 추가하고 길이를 반환

```js
numbers //[4, 3, 2, 1]
numbers.push('push') //5 (길이를 반환)
numbers //(5) [1, 2, 3, 4, "push"] (길이와 배열 반환)
```



#### *arr*.pop()

> 뭐를 인자로 넘기던 제일 마지막거 뽑는다. 범위 밖도 포함.

```js
numbers.pop() //4
```



#### *arr*.unshift(*val*)

> 배열의 처음에 요소를 추가하고 길이를 반환

```js
numbers //[1, 2, 3, 4]
numbers.unshift('c') //5
numbers //['c', 1, 2, 3, 4]
```



#### *arr*.shift()

> 배열의 처음의 요소를 뽑는다.

```js
numbers //['c', 1, 2, 3, 4]
numbers.shift() //'c'
numbers //[1, 2, 3, 4]
```



#### *arr*.includes(*val*)

> 배열에 포함되어있는지 확인

```js
numbers //[1, 2, 3, 4]
numbers.include(1) //true
numbers.include(0) //false
```



#### *arr*.join(*val*)

> python의 join함수와 같다

```js
numbers //[1, 2, 3, 4]
numbers.join() //"1,2,3,4"
numbers.join('') //"1234"
numbers.join('-') //"1-2-3-4"
```



#### *arr*.indexOf(*val*)

> 해당 val의 인덱스를 반환한다.

```js
numbers //[1, 2, 3, 4]
numbers.indexOf(1) //0
numbers.indexOf(9) //-1 (없는 값)
```



#### *arr*.sort()

> 배열을 정렬하고 길이와 정렬된 배열 반환.

```js
numbers //[3, 4, 1, 2]
numbers.sort() //(4) [1, 2, 3, 4]
numbers //(4) [1, 2, 3, 4]
```



#### *arr*.slice(*start*, *end*)

> 잘린 배열을 반환.

```js
numbers //[1, 1, 2, 4, 5]
numbers.slice(2) //(3) [2, 4, 5]
numbers.slice(1, 3) //(2) [1, 2]
numbers.slice(-2) //(2) [4, 5] (음수 접근이 indexOf에서는 안되지만 slice는 가능)
```



#### *arr*.forEach(*function*)

> 배열의 각각의 원소에 대해 함수를 실행하는 메서드

```js
let foods = ['빠삐코', '스크류바', '메로나']
foods.forEach(element => console.log(element))
//빠삐코
//스크류바
//메로나
```

> 변수의 갯수에 따라 표현되는 요소가 늘어난다

```js
foods.forEach((element,idx) => console.log(element,idx))
//빠비코 0
//스크류바 1
//메로나 2
```

```js
foods.forEach((element, idx, food) => console.log(element, idx, food))
//빠삐코 0 
  ▶ (3) ["빠삐코", "스크류바", "메로나"]
//스크류바 1
  ▶ (3) ["빠삐코", "스크류바", "메로나"]
//메로나 2
  ▶ (3) ["빠삐코", "스크류바", "메로나"]
```



#### *arr*.map(*function*)

> python의 map를 생각하자.

```js
const numbers = [1, 2, 3]
const strNumbers = numbers.map(number => String(number)) 
strNumbers //["1", "2", "3"]
```

```js
const squareNumbers = numbers.map(number => number * number)
squareNumbers //[1, 4, 9]
```

```js
const seulgi = [
    {'velocity': 40, 'time': 50},
    {'velocity': 50, 'time': 100},
    {'velocity': 20, 'time': 580}
]
const distances = seulgi.map(obj => obj.velocity * obj.time)
```



#### *arr*.filter()

> 필터 즉 해당하는 값으로 된 배열을 리턴한다.

```js
const nums = [1, 5, 6, 8]
const evenNums = nums.filter(num => num % 2 === 0)
evenNums //[6, 8]
```

```js
const drinks = [
    {type: 'caffeine', name: 'coldbrew'},
    {type: 'caffeine', name: 'green tea'},
    {type: 'juice', name: 'orange'},
    {type: 'juice', name: 'lemon'},
]
const nonCaffeines = drinks.filter(each => each.type !== 'caffeine')
```



#### *arr*.reduce(*function*, *initialvalue*)

> forEach와 비슷하지만 누적값과 현재값을 받아서 누적된 결과값을 리턴한다.
>
> initialvalue를 넘겨주지 않으면 첫번째 인자를 건너 뛴다.

```js
const reduceNum = [1, 5, 6]
const reduceResult = reduceNum.reduce((result, num) => result + num*10, 0)
reduceResult //120
```



#### *arr*.find()

> 찾아주는 함수

```js
const dc = ['슈퍼맨', '베트맨', '조커']
const badguy = dc.find(name => name === '조커')
badguy //"조커"
```



#### typeof *type*

> 타입을 반환

```js
typeof numbers //"object"
```

```js
typeof [1, 23, 4] //"object"
typeof 1 //"number"
```





## 5. Dict

> Key - Value 로 이루어진 데이터 구조이다.

#### 기본 구조

```js
// 자바스크립트 object 표기법
let seulgi = {
    name: 'seulgi',
    age: 26,
    number: '010-1111-2222'
}
```

ES6+ 이후로는 아래의 방법을 권장한다.

```js
// 변수를 그대로 넣으면 변수명: 값
let name = 'taehyun'
let stuffs = ['공기청정기', '커피머신']
let taehyun = {
    name,
    stuffs
}
```



#### JSON.stringify(*val*)

> Json형식의 데이터를 string형식으로 바꿔주는 메서드, undefined를 리턴하긴 한다

```js
let jsonData = JSON.stringify(taehyun) 
jsonData //"{"name":"taehyun","stuffs":["공기청정기","커피머신"]}"
```



#### JSON.parse(*val*)

> string형식의 데이터를 Json형식으로 바꿔주는 메서드.

```js
let jsonParse = JSON.parse(jsonData)
jsonParse //{name: "taehyun", stuffs: Array(2)}
```





## 6. Function

#### 함수 선언식

```js
function add(num1, num2) {
    return num1 + num2
}
console.log(add(1, 3)) //4
typeof add //function
```



#### 함수 표현식

> 함수 자체를 변수로 저장해서 사용한다. (1급 객체)

```js
let add = function adder(num1, num2) {
    return num1 + num2
}
console.log(add(1, 3)) //4
console.log(adder(1, 3)) //Error
typeof add //function
```



#### 화살표 함수(Arrow Function)

> ES6+, 위의 함수와 100% 동일한 것이 아님.

```js
let sub = (num1, num2) => {
    return num1 - num2
}
```

##### 기본인자(default args)

```js
let person = (name='동명') => {
    return `${name}, 안녕!`
}
person() //동명, 안녕!
person('승만') //승만, 안녕!
```



##### syntactic sugar

> 인자가 하나인 경우, 괄호`()` 생략가능
>
> 단순 리턴인 경우(한줄에 끝나는 경우), `{}` 및 `return` 키워드 생략 가능

```js
let greeting = name => `${name}, 안녕!`
console.log(greeting('동명')) //동명, 안녕!
```

```js
let mul = (num1, num2) => num1 * num2
console.log(mul(2, 4)) //8
```

> 인자가 없는 경우에는 `()` 작성

```js
let hello = () => 'hello, world!'
console.log(hello()) //hello, world!
```

> `object` 리턴 시 반드시 `()` 묶어서 작성

```js
let me = (name, age) => ({name, age})
console.log(me('hi', 33)) //{name: "hi", age: 33}

let me = (name, age) => (name, age)
console.log(me('hi', 33)) //33
let me = (name, age) => {name, age}
console.log(me('hi', 33)) //'hi'
```

##### 익명함수

```js
((a, b) => a * b)
(function(num) {return num*num}) (자바스크립트가 알아서 ;를 하기 때문에 괄호를 씌운다.)
```

> 즉시 실행 (익명함수 + 호출) - IIFE(Immediately Invoked Function Expression)

```js
(function(num) {return num*num})(5) //25
```





## 7. type

> JS는 이상하니까 그냥 알아두는게 좋다. 신경써야할 것만 정리

```js
typeof NaN //number
isNaN(NaN) //true
NaN === NaN //false
isNaN(0) //false
typeof Infinity //number
typeof [] //object
typeof (() => {}) //function
typeof typeof '123' //string
```

```js
1 + '1' //"11"
2 * '12' //24
parseInt('123') //123
String(2) //"2"
```









## 9. 실습

#### Arrow Function으로 바꿔보기

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
    return `${member_base}와 ${member}가 베트남에 가요`
}
console.log(veitnam('누군가')) //황여진와 누군가가 베트남에 가요
```

#### 배열을 받아 다 계산하는 함수 작성하기

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

// 콜백
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

