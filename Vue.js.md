# Vue.js

> 190503 강의내용

[TOC]





## 0. Vue.js

- 자바스크립트 프레임워크, 철저히 뷰(View)에 최적화 되어있다.

- 명령형 언어

  Django에서 context를 넘겨 template에서 썼던 것과 유사하다. app을 Vue와 연결해 data를 넘겨 사용하는 것.

- MVVM (Model - View - ViewModel)의 VM에 속한다

  MVC의 C(Controller)와 비슷한 역할을 하며 data가 ViewModel이다.





## 1. 준비하기

- CDN

  개발버전, warning이 더 정확하게 뜨지만 조금 느림.

  ```html
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  ```

  



## 2. 기본구조

> `el`: Vue와 연결할 element
>
> `data`: app(vue instance)의 속성
>
> `methods`: app의 메서드. this가 동작하는 방식이 달라 `arrow function`은 사용할 수 없다.
>
> `computed`: 메서드와 달리 계산 된 결과를 저장해 놓는 캐싱방법을 사용하여 결과를 리턴한다.

```js
const app = new Vue ({
    el: '#app',
    data: {
    	...
	},
    methods: {
    	...
		}
	},
    computed: {
        ...
    }
})
```

사용하려면 다음과 같이 `div의 속성`과 `Vue의 element`를 같은 값으로 설정해 연결해 주어야 한다.

```html
<div id="app">
    ...
</div>
<script>
    const app = new Vue ({
        el: '#app',
        ...
    })
</script>
```

#### 데이터 접근하기==(반드시 기억)==

```js
const app = new Vue ({
    el: '#app',
    data: {
        message: 'hello, vue'
    },
    methods: {
        ...
    }
})
```

위의 예제에서 `app`의  `message`에 접근하려면

```js
app.$data.message
```

로 접근이 가능하다. 

하지만 data값은 접근을 자주하므로 $data가 없더라도 접근이 가능하게 되어있다.

```js
app.message
```





## 3. Directive(디렉티브) (v-___)

>`v-____`는 디렉티브(Directive)라고 부르며 vue의 element에 지시를 하는 문법이다.
>
>값에 해당하는 부분("")에 자바스크립트 문법을 사용할 수 있다.
>
>`v-____`는 축약형으로 `@____`으로 표현할 수 있다.



#### v-on:*func*="*method*"

> 이벤트 리스너를 등록한다.

클릭하면 count가 증가하는 예제이다.

```html
<div id="app">
    <button v-on:click="plus">v-on:click</button>
    {{ count }}
</div>
<script>
    const app = new Vue ({
        el: '#app',
        data: {
            count: 0
        },
        methods: {
            plus: function() {
                this.count++
            }
        }
    })
</script>
```

<button>v-on:click</button>1



#### v-text=""

> vue의 data안의 해당하는 key값을 입력받아 value를 그대로 출력함. 

```html
<div id="app">
	<span v-text="message"></span>    
</div>
<script>
    const app = new Vue ({
        ...
        data: {
            message:'hello,vue!'
        },
        ...
    })
</script>
```

```
hello,vue!
```



#### v-html=""

> 해당하는 key의 value에 html태그가 있으면 html로 출력한다. {{}}를 사용하는 것보다 권장하는 방식이다.

```html
<span v-html="htmlMessage"></span>
```



#### v-once

> 렌더링을 한번만 한다. 즉 값이 고정되고 이후에 data가 바뀌더라도 바뀌지 않음.

버튼을 클릭해도 처음값인 0으로 고정되어 값이 바뀌지 않는다.

```html
<h1 v-once v-text="count"></h1>
```



#### v-if=""

> if문이다. "" 안에 조건문을 쓴다.

```html
<span v-if="count > 5">5보다 큼!</span>
<span v-else-if="count === 5">딱 5임!!</span>
<span v-else>5보다 작음!</span>
```



#### v-show="*boolean*"

> ""안의 boolean값에 따라 css가 바뀌며 화면에 표시할지 결정한다.

* `v-if`는 조건에 맞는 태그만 렌더링하지만, `v-show`는 렌더링을 하고 `display:hidden`속성을 이용해 표시한다.

- bootstrap의 modal이 v-show를 사용한다.

```html
<h1 v-show="isTrue"> True!! </h1>
<script>
    const app = new Vue ({
        ...
        data: {
            isTrue: True
        },
        ...
    })
</script>
```

```
True!!
```



#### v-for=""

> 반복문, ""안에 반복문을 선언해준다.

```html
<li v-for="hero in myArray">
	{{ hero }}
</li>
<script>
    const app = new Vue ({
        ...
        data: {
            myArray: [
                '캡틴아메리카',
                '헐크',
                '아이언맨'
        	],
        	...
        },
        ...
    })
</script>
```

```
ㆍ 캡틴아메리카
ㆍ 헐크
ㆍ 아이언맨
```



#### v-bind:href=""

> html 속성의 값을 data에 있는 값으로 설정해준다.

```html
<a v-bind:href="urlLink">구글</a>
<script>
    const app = new Vue ({
        ...
        data: {
            urlLink: 'https://google.com'
        },
    })
</script>
```

[구글](https://google.com)

- 축약형으로 v-bind를 빼고 써도 된다.

```html
<a :href="urlLink">구글</a>
```



#### v-model=""

> View와 Data를 양방향으로 이어준다. 즉, 키보드로 입력한 값이 즉시 저장되고 출력된다.
>
> 반드시 ""안의 변수가 data에 선언되어있어야 한다.

```html
<input v-model="blahblah">
{{ blahblah }}
<script>
    const app = new Vue ({
        ...
        data: {
            blahblah: '',
        },
    })
</script>
```

- 자바스크립트의 문법을 적용해서 문자를 더해줄 수 있다.

```html
{{ blahblah + '!!!!' }}
```

- 파이썬의 문법을 적용해서 거꾸로 출력해줄 수 있다.

```html
{{ blahblah.split('').reverse().join('') }}
```

##### computed 사용

- `computed`를 사용하여 좀 더 편안하게 결과값을 가져올 수 있다.

  메서드는 어떠한 동작을 하는 것이지만, computed는 계산한 결과를 가져오는 것.

```html
{{ reverseBlahblah }}

<script>
    const app = new Vue ({
        el: '#app',
        data: {},
        methods: {},
        computed: {
            reverseBlahblah: function() {
                return this.blahblah.split('').reverse().join('')
            }
        }
    })
</script>
```

- 새로운 날짜를 계속 갱신해서 표기해야하는 경우에는 부적절하다. 같은날짜만 출력되기 때문

```js
const app = new Vue ({
    ...
    computed: {
        computedToday: function() {
            return new Date()
        }
    }
})
```

```
app.computedToday //같은 날짜만 출력됌
```



##### select 예제

```html
<select v-model="lunch">
    <option value="특식">특식</option>
    <option value="한식">한식</option>
    <option value="양식">양식</option>
</select>
<h1>{{ lunch }}</h1>
```



#### 

## 4. functions

> 자바스크립트에서 활용가능한 함수들

#### 

#### new Date()

```js
const app = new Vue ({
    ...
    methods: {
        today: function() {
            return new Date()
        }
    }
})
```

```js
app.today() //오늘 날짜와 시간이 나옴
```

