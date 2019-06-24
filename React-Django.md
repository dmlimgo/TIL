# React-Django

> React와 Django를 연결해보자.



## 프로젝트 생성하기

프로젝트 폴더 생성 후 접근

```bash
$ mkdir Deact
$ cd Deact
```

React앱 생성

```bash
$ create-react-app deact-frontend
```

django프로젝트 생성 후 가상환경 만들기

```bash
$ mkdir deact-backend
$ cd deact-backend
$ python3 -m venv 가상환경이름
$ source 가상환경이름/bin/activate
```

Django 설치 후 실행

```bash
$ pip install django
$ django-admin startproject deact

$ cd deact
$ python manage.py migrate
$ python manage.py runserver
```



다음 작업은 commit한 상태에서 진행해야 하므로 commit 진행.

Deact-frontend 폴더로 와서 다음 명령어 실행

```bash
$ yarn eject
y
```



## React와 Django 통합하기

React-backend 폴더로 와서 다음 패키지 설치

```bash
$ pip install django-webpack-loader
```

settings.py에 `webpack_loader` 를 추가하고 templates 경로도 설정해준다.

```python
'DIRS': [os.path.join(BASE_DIR, "templates")],
```

`templates/index.html` 에 라우팅을 추가해준다.

```html
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Deact</title>
</head>
<body>
    <div id="root">
    </div>
    {% render_bundle 'main' %}
</body>
</html>
```

urls.py에 아래와 같이 연결해 준다.

```python
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
]
```



React로 와서 webpack에 대한 설정을 해준다.

`web pack-bundle-tracker` 를 설치한다.

```bash
# deact-frontend/
$ yarn add --dev webpack-bundle-tracker
```

설치한 모듈을 config/path.js에 추가해준다.

```js
module.exports = {
	...
  statsRoot: resolveApp("../deact-backend/deact")
};
```

config/webpack.config.dev.js

```js
const BundleTracker = require('webpack-bundle-tracker')

const publicPath = 'http://localhost:3000/';
const publicUrl = 'http://localhost:3000/';

    entry: [
      // require.resolve("./polyfills"), (create-react-app이 업데이트되면서 polyfill.js가 사라짐 필요없음)
      require.resolve("webpack-dev-server/client") + "?http://localhost:3000",
      require.resolve("webpack/hot/dev-server"),
      require.resolve('react-dev-utils/webpackHotDevClient'),
      paths.appIndexJs
    ],
      
plugins: [
			...
      new BundleTracker({path: paths.statsRoot, filename: 'webpack-stats.dev.json'})
]
```

config/webpackDevServer.config.js

```js
// host 밑에 다음을 추가(확실치 않음. 첫줄은 추가 해야되는건지 아닌지..)
    host: host,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
```



#### 여기까지 dev모드, 이제는 build된 react를 띄우는 Prod모드

생략...