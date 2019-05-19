# Firebase

> backend(DB)를 써야하는데(구조상 브라우저 안에 localStorage에 있음 근데 사람들끼리 공유가 안됌),  이걸 장고, 서버 필요없이 클라우드 서비스(파이어베이스)를 쓰면서 저장을 해 보겠다.
>
> paas(platform as a service), NoSQL이다.

콘솔로 이동 > 프로젝트 추가

![fb1](\image\fb1.PNG)



창이 열리면

왼쪽 개발 탭 > Database > 데이터베이스 만들기 > 테스트 모드로 시작 > 사용 설정

위에서 Realtime Database로 바꿔준다.

---

vuefire 검색해서 [github](<https://github.com/vuejs/vuefire>) > branch:v1으로 바꿔준다.

밑에 Installation의 아래 두개의 script를 가져다 `head`에 넣어준다. 그리고 firebasejs뒤에 `5.8.0`으로 바꿔준다.(공식문서가 5.8.0 이라서)

```html
<head>
...
<!-- Firebase -->
<script src="https://gstatic.com/firebasejs/5.8.0/firebase.js"></script>
<!-- VueFire -->
<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
</head>
```

vue도 위로 끌어올려주자 밑에 있으면 인식 안될수도 있음.

```html
<head>
...
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<!-- Firebase -->
<script src="https://gstatic.com/firebasejs/5.8.0/firebase.js"></script>
<!-- VueFire -->
<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
</head>
```



다시 navbar에 문서로 이동 클릭

웹시작하기 클릭

밑의 내용은 설정과 관련된 오브젝트를 만드는데 밑의 선택사항을 사용해서 써라 라는 내용임

```html
<script>
  // Initialize Firebase
  // TODO: Replace with your project's customized code snippet
  var config = {
    apiKey: "<API_KEY>",
    authDomain: "<PROJECT_ID>.firebaseapp.com",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    projectId: "<PROJECT_ID>",
    storageBucket: "<BUCKET>.appspot.com",
    messagingSenderId: "<SENDER_ID>",
  };
  firebase.initializeApp(config);
</script>
```

3개만 남기고 지운다. 필요없음.

```html
<script>
  // Initialize Firebase
  // TODO: Replace with your project's customized code snippet
  var config = {
    apiKey: "<API_KEY>",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    projectId: "<PROJECT_ID>",
  };
  firebase.initializeApp(config);
</script>
```

databaseURL은 프로젝트의 아래 주소랑 같다.

![fb2](C:\Users\student\Desktop\TIL\image\fb2.PNG)

projectId는 `vue-project-myeong` 이다.

apiKey는 왼쪽 탭에 톱니바퀴 > 웹API키 이다.

var도 불편하니까 const로 바꾼다.

다 바꿔주자.

---

DB초기화 

```html
const db = firebase.database()
```

기존에 있던 이코드는 이제 필요없음

```js
const STORAGE_KEY = 'vue-todo'
const todoStorage = {
    fetch: function() {
        const todoList = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
        todoList.forEach(function(todo, index) {
            todo.id = index
            todoList.uid = index
        })
        return todoList
    },
    save: function(todoList) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todoList))
    }
}
```

여기 totoStorage도 필요없음.

```js
data: {
   newTodo: '',
   status: 'all',
   // todoList: todoStorage.fetch()
}
```

아래걸 선언해주자.

```js
firebase: {
	todoList: db.ref('todoList')
},
```

문서에 보면 이런게 있다. (배열에 요소 추가하기)

```js
// add an item to the array
vm.$firebaseRefs.anArray.push({
  text: 'hello'
})
```

따라서 아래의 코드의 `this.todoList.push`를 `this.$firebaseRefs.todoList.push`로 바꿔준다.

```js
addNewTodo: function() {
    if (this.newTodo) {
        this.$firebaseRefs.todoList.push({
            id: Date.now(),
            content: this.newTodo,
            completed: false
        })
        this.newTodo = ''
    }
},
```

---

삭제 코드도 변경

![fb3](C:\Users\student\Desktop\TIL\image\fb3.PNG)

위에 보면 todoList 안에 키로 접근이 가능한 걸 알 수 있다.

github에 삭제예제를 보자

```js
// Vue instance methods
 deleteItem: function (item) {
   this.$firebaseRefs.items.child(item['.key']).remove()
 },
```

따라서 아래의 코드를 변경해준다.

```js
deleteTodo: function(todo) {
    this.todoList.splice(this.todoList.indexOf(todo), 1)
},
```

이렇게

```js
deleteTodo: function(todo) {
    this.$firebaseRefs.todoList.child(todo['.key']).remove()
},
```

---

체크표시도 수정

바꿀 때마다 firebase에 반영을 해줘야 함.

github 예시

```js
updateItem: function (item) { 
    // create a copy of the item
    const copy = {...item}
    // remove the .key attribute
    delete copy['.key']
    this.$firebaseRefs.items.child(item['.key']).set(copy)
} 
```

업데이트하려면 지우고 다시 만들어야 한다고 한다. 위의 내용을 참고해서 작성한다.

```js
updateTodo: function(todo) {
    // '...'은 object를 펼쳐서 각각 하나씩 던져준다.
    const copy = {...todo}
    delete copy['.key']
    this.$firebaseRefs.todoList.child(todo['.key']).set(copy)
},
```

체크박스도 바꿔준다.

```html
<input type="checkbox" v-model="todo.completed">
```

를 아래처럼

```html
<input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)">
```

---

채팅 구현(6_chat.html)

기본 설정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Firebase -->
    <script src="https://gstatic.com/firebasejs/4.2.0/firebase.js"></script>
    <!-- VueFire -->
    <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
    <script>
        // Initialize Firebase
        // TODO: Replace with your project's customized code snippet
        const config = {
          apiKey: "AIzaSyDV19Qqh3dkhV8AxWEmSCfDYkkoELaTjWI",
          databaseURL: "https://vue-project-myeong.firebaseio.com/",
          projectId: "vue-project-myeong",
        };
        firebase.initializeApp(config);
        const db = firebase.database()
    </script>
</head>
<body>
    
</body>
</html>
```

유저가 있으면 작성가능하고 없으면 다른 화면 띄워주게 해보자

Firebase > Authentication > 로그인 방법 > 이메일/비밀번호 설정

firbase에서 제공하는 [firebaseui](<https://github.com/firebase/firebaseui-web>)

CDN 복사 > 문서에 붙여넣기

```html
<script src="https://cdn.firebase.com/libs/firebaseui/3.6.0/firebaseui.js"></script>
<link type="text/css" rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/3.6.0/firebaseui.css" />
```

아래 세줄을 db초기화 밑에 선언해준다.

```html
const auth = firebase.auth()
const ui = new firebaseui.auth.AuthUI(auth)
ui.start('#firebaseui-auth-container')
```

그리고 body에

```html
<div ip="app">
    <div id="firebaseui-auth-container"></div>
</div>
```

---

채팅 구현

나중에 보고 정리

---

배포하기

node 검색 > [node.js](<https://nodejs.org/en/>) > `10.15.3 LTS`다운로드 > 설치

cmd에서 node -v를 입력하면 확인 할 수 있다.

```bash
$ node -v
```

우선 npm 확인해보고

```bash
$ npm -v
```

싸피컴기준 6.4.1이 뜬다.

툴 설치

```bash
$ npm install -g firebase-tools
```

```bash
$ firebase login --interactive
```

하면 뜨는 질문에서 Y해주면 로그인 창이 뜬다. 로그인해주자.

여기서부터는 무조건 cmd로 가야한다. 그리고 작업중인 폴더로 가서 아래의 명령어를 쳐준다.

```bash
$ firebase init
```

질문이 뜨는데 Y해주자.

`Database`, `Hosting` 둘다 선택

![fb4](C:\Users\student\Desktop\TIL\image\fb4.PNG)

그다음 vue-project-myeong에서 엔터

그리고 엔터 두번 y한번

설정끝.

![fb5](C:\Users\student\Desktop\TIL\image\fb5.PNG)

public에 index.html을 넣어준다. (배포할 파일)

```bash
$ firebase deploy
```

를 해주면 뭔가 한다. 배포끝.

![fb6](C:\Users\student\Desktop\TIL\image\fb6.PNG)

Hosting URL로 접속하면 된다.

