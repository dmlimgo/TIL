## Project-Insta

> 090411 프로젝트 시작
>
> 총정리 느낌?

#### 1. 환경설정하기

개별 project에서 독립적인 가상환경 구성하기

Django 최신버전이 Sqlite 상위버전을 사용하기 때문에 안정적인(사용하던) 버전을 일단 사용했다.

```bash
$ pyenv virtualenv 3.6.7 insta-venv
$ pyenv local insta-venv
$ pip install --upgrade pip
$ pip install django==2.1.8
```

간단한 세팅 후 확인

```bash
$ pip list
Package    Version
---------- -------
Django     2.1.8  
pip        19.0.3 
pytz       2019.1 
setuptools 39.0.1 
```

버전 정보 저장.

```bash
$ pip freeze > requirements.txt
```

app 등록

urls.py 생성

migrate 까지 해주자 (admin, user 등등이 미리 되어있으므로)

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



#### 2. 모델, Admin 설정

> MTV 중 Model부터 정의하고 가자

```python
# models.py
```

migrate 해주자

```bash
makem~
migrate
```

admin 설정도

```python
# admin.py
from .models import Post
admin.site.register(Post)
```

표시형식을 바꿔주고 싶다면

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
```



#### 3. template 설정

기본적으로는 APP_DIRS에 의해 각각의 app의 templates 폴더를 보게 되는데

다른 폴더를 추가적으로 보게 하고 싶다면 DIRS에 추가해주면 된다.

```python
# settings.py
TEMPLATES = [
	    ...
        'DIRS': [os.path.join(BASE_DIR, 'instagram', 'templates')],
        'APP_DIRS': True,
 		...
```

###### 3.1 navbar.html 분리

navbar를 그대로 붙여넣으면 base.html이 복잡해지니까 분리

_navbar.html 생성

꼭 _일필요는 없다.

그리고 base.html에서 {% include '_navbar.html' %}

#### 