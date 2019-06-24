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

