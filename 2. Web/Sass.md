# Sass

> Syntactically Awesome StyleSheets의 약자로 CSS pre-processor이다.

### 1. 설치하기

```bash
$ npm install -g node-sass
$ node-sass -v
```

--save-dev? 해야하나..

### 2. 사용하기

assets/sass에 sass파일을 생성하여 내용을 입력한 후 다음 명령어를 실행한다. 

`expanded`는 표준 스타일의 css 파일을 생성한다.

```bash
$ node-sass --output-style expanded sass폴더경로 --output css폴더경로
```

ex

```bash
$ node-sass --output-style expanded src/assets/sass --output src/assets/css
```



### 3. Watch

sass 파일의 변경을 감지하여 변경될 때마다 자동으로 css 파일을 업데이트한다.

```bash
$ node-sass --watch sass폴더경로 --output css폴더경로
```

