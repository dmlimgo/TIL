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

