# Vue.js

> 190503 강의내용





## Vue.js

- 자바스크립트 프레임워크, 철저히 뷰(View)에 최적화 되어있다.

- 명령형 언어

  Django에서 context를 넘겨 template에서 썼던 것과 유사하다. app을 Vue와 연결해 data를 넘겨 사용하는 것.

- MVVM (View model)의 VM에 속한다

  controller와 비슷한 역할을 하며 data가 view model이다.





## 준비하기

- CDN

  개발버전, warning이 더 정확하게 뜨지만 조금 느림.

  ```html
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  ```

  



## 기본구조

```html
<script>
    const app = new Vue ({
        // 실제 Vue와 연결할 element
        el: '#app',
        // app(vue instance)의 속성
        data: {
            message: 'Hello, Vue!',
            count: 0
        },
        // app의 method. this가 동작하는 방식이 달라 arrow function은 사용할 수 없다.
        methods: {
            plus: function() {
                this.count ++
            }
        }
    })

</script>
```



