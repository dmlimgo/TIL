# Express.js



## 설치하기

express.js를 사용하기 위해서는 node.js가 필요하다.

설치되어 있다면 넘어간다.

```bash
$ brew install node
$ node -v
```



myapp 폴더를 만들고 들어간다.

```bash
$ mkdir myapp
$ cd myapp
```



Express.js 설치

```bash
$ npm install express -g
```

npm(node package manager)에서 express를 설치한다.

-g는 global을 의미하며 global로 설치한 모듈은 어느 위치에서든 명령어를 실행할 수 있다.

설치가 완료되면. `node_modules` 폴더가 생성되어 있다.



## 시작하기

아래 명령어를 입력하면 app생성을 위한 환경을 설정한다.

```bash
$ npm init
```

몇가지 정보를 입력하라고 하는데 각각이 의미하는 바는 다음과 같다.

선택사항이므로 일단은 entry point 만 자신의 app이름에 맞게 설정해주자.



`name`: 프로젝트 이름 (기본설정은 현재 폴더명)

`version`: 현재 버전 (기본설정은 1.0.0)

`description`: 프로젝트 설명

`entry point`: 프로그램 실행 파일 (기본설정은 index.js)

`test command`: 테스트를 하기 위한 명령어

`git repository`: 온라인 git 저장소 주소

`keywords`: 프로젝트 키워드

`author`: 프로젝트 제작자 이름

`license`: license (기본 설정은 ISC)

완료되면 package.json과 package-lock.json파일이 생성되어 있다.



express를 package.json의 dependencies에 등록한다.

```bash
$ npm install express --save
```

—save를 입력하지 않으면 설치만 되고 등록되지 않는다.



github.com 등에서 다운 받은 코드들은 아래 명령어로 dependencies의 모듈들을 설치해줄 수 있다.

```bash
$ npm install
```



## Hello world!

아무 문구나 출력해보자

app.js파일(package.json의 entry point와 같아야 함)을 만들고 아래의 내용을 입력한다.

```js
let express = require("express")
let app = express()

app.get('/', function(req, res){
    res.send('welcome back!')
})

app.listen(3000)
```

require를 통해 모듈을 불러오고

app으로 모듈의 인스턴스를 받아 기능들을 사용한다.

app.listen의 인자에 port를 입력하면 localhost:*port* 로 접속할 수 있다.

아래의 명령어를 입력하여 서버를 실행한다.

```bash
$ node app.js
```

Chrome의 주소창에 localhost:3000을 입력하여 출력된 것을 볼 수 있다.



## nodemon 활용하기

Node.js의 js파일들은 수정해도 자동으로 서버에 반영해주지 않기 때문에 nodemon을 사용하여 자동으로 반영할 수 있다.

는 나중에.



## ejs 사용하기

view를 구성해보자

```bash
$ npm install ejs --save
```

설치 후

```bash
$ mkdir views
$ cd views
$ touch index.ejs
```

폴더구성

```bash
myapps
 ㄴapp.js
 ㄴviews
   ㄴindex.ejs
```

app.js의 코드를 변경해준다.

4번째 줄 코드로 ejs를 사용하고, 5번째 줄 코드에서 views폴더의 위치를 정해준다.

이후 render를 이용하여 파일명을 인자에 넣어주면 index가 보이게 된다.

```js
let express = require("express")
let app = express()

app.set('view engine', 'ejs')
app.set('views', './views')

app.get('/', function(req, res){
    res.render('index')
})

app.listen(3000)
```

index.ejs

```ejs
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    this is index!
</body>
</html>
```



## POST요청 보내기

index.ejs를 재구성한다.

```ejs
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    this is index!
    <form action="" method="POST">
        <input type="email" name="email">
        <input type="password" name="password">
        <input type="submit">
    </form>
</body>
</html>
```

index2.ejs를 생성하여 post로 보낸 요청을 받아 출력하는 코드를 작성한다.

```ejs
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <%= email %>
    <%= password %>
</body>
</html>
```

app.js를 다음과 같이 재구성한다.

```js
let express = require("express")
let app = express()

app.set('view engine', 'ejs')
app.set('views', './views')

app.get('/', function(req, res){
    res.render('index')
})

app.post('/', function(req, res){
    let context = {}
    let email = req.body.email
    let password = req.body.password

    context.email = email
    context.password = password

    res.render('index2', context)
    console.log(email, password)
})

app.listen(3000)
```

하지만 body에 있는 내용을 가져오기 위해서는 body-parser가 필요하다.

```bash
$ npm install body-parser --save
```

body-parser 사용을 위한 코드를 추가해준다.

app.js

```js
let express = require("express")
let bodyParser = require("body-parser")
let app = express()

app.set('view engine', 'ejs')
app.set('views', './views')

app.use(bodyParser.urlencoded())
app.use(bodyParser.json())

app.get('/', function(req, res){
    res.render('index')
})

app.post('/', function(req, res){
    let context = {}
    let email = req.body.email
    let password = req.body.password

    context.email = email
    context.password = password

    res.render('index2', context)
    console.log(email, password)
})

app.listen(3000)
```

추가로 console.log를 이용하면 node.js에서는 인터넷 브라우저가 아닌 터미널에서 출력되는 것을 확인할 수 있다.

deprecated가 뜨는데 일단은 무시하자.



## 코드 분리하기(라우터 사용하기)

Django 프로젝트에서 app별로 url이나 views를 따로 사용했듯이 분리해주도록 하자.

다음과 같이 코드를 분리한다.

```
myapps
 ㄴapp.js
 ㄴrouters
   ㄴindex
     ㄴindex.js
 ㄴviews
   ㄴindex.ejs
   ㄴindex2.ejs
```

app.js

```js
let express = require("express")
let app = express()

let index = require("./routers/index/index.js")

app.use ('/', index)

app.set('view engine', 'ejs')
app.set('views', './views')

app.listen(3000)
```

index라는 변수에 경로를 설정해 주고, app.use를 이용해서 / 경로 뒤에 붙여준다.

index.js

```js
let express = require("express")
let bodyParser = require("body-parser")
let router = express.Router()

router.use(bodyParser.urlencoded())
router.use(bodyParser.json())

router.get('/', function(req, res){
    res.render('index')
})

router.post('/', function(req, res){
    let context = {}
    let email = req.body.email
    let password = req.body.password

    context.email = email
    context.password = password

    res.render('index2', context)
    console.log(email, password)
})

module.exports = router
```

router에 router인스턴스를 선언해주고 module.exports로 router가 동작할 수 있도록 해준다.

이후 app.~ 대신 router.~로 바꿔준다.