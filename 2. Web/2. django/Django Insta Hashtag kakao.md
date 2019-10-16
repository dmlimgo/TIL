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



### 2. Hashtag

> post와 tag의 N:M관계

#### 2.1 모델링

Post

| id   | content               |
| ---- | --------------------- |
| 1    | #나는 #눈물을         |
| 2    | #나는 #항상 #배고프다 |
| 3    |                       |

Tag

| id   | content |
| ---- | ------- |
| 1    | #나는   |
| 2    | #눈물을 |
| 3    | #항상   |
| 4    | #흘린다 |

관계

|      | post_id | tag_id |
| ---- | ------- | ------ |
|      | 1       | 1      |
|      | 1       | 2      |
|      | 2       | 1      |
|      | 2       | 3      |

#### 2.2 코드

models.py

```python
class Hashtag(models.Model):
    content = models.TextField(unique=True)
    
class Post(models.Model):
    ...
    hashtags = models.ManyToManyField(Hashtag, related_name='posts')
```

views.py

```python
from .models import Hashtag
post_contents = post.content.split()
for each_word in post_contents:
    if each_word.startswith('#'):
        hashtag, is_created = Hashtag.objects.get_or_create(content=word)
        # 'get_or_create' methods returns 
        # is nonexist (hashtag object, True)
        # or is exist (hashtag object, False)
        post.hashtags.add(hashtag)
```

##### update하기

아예 싹 지우고 다시 만든다.

views.py

```python
def edit(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            post.hashtags.clear()
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag, is_created = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag)
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form}
    return render(request, 'posts/form.html', context)
```



##### 글의 hashtag를 링크로 바꾸기

전에 gravatar

templatetags/hashtag_link.py

```python
from django import template
# template을 관리할거야

register = template.Library()
# Library에 등록할거고

# filter를 등록할거고
@register.filter
def hashtag_link(post):
    content = post.content
    hashtags = post.hashtags.all()
    
    for hashtag in hashtags:
        content = content.replace(
                        hashtag.content,
                        f'<a href="hashtags/{hashtag.pk}/">{hashtag.content}</a>'
                        )
    return content
```

html

```html
 {% load hashtag_link %}
<!--{{ post.content }}-->
safe가 있어야 링크로 동작함
{{ post|hashtag_link|safe }}
```



### 3. 소셜 로그인

#### 3.1 세팅

kakao Developers 가입

앱 생성하기 -> 생성

API키 메모장에 복사

설정-일반-플랫폼 추가- 웹 선택, 도메인은 

![django_3](image\django_3.PNG)

고급-Client Secret-코드 생성

코드 메모장에 복사 -> 상태 ON -> 적용

---

#### 3.2 django

여기저기서 다 쓰는 거임 pip install django-allauth 설치

pip freeze도 해주고

<https://django-allauth.readthedocs.io/en/latest/installation.html>

위의 내용대로 한다.

중간에 . . .은 지워준다.

```python
# settings.py
INSTALLED_APPS [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    ...
]
...
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
...
SITE_ID = 1
...
```

```python
# urls.py
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
# 여기서는 중복되어도 상관없다. 위에거 확인하고 밑에서 확인한다. 단 최종주소까지 같으면 안된다.
```

migrate 해주자.



admin을 들어가보면 많이 추가되어 있다.

소셜 어플리케이션 - 추가

제공자 : kakao, 이름: 아무거나

클라이언트 아이디: APIKEY, 비밀 키:Client Secret

Sites에 example.com 오른쪽으로 옮겨주고

저장



##### 사용자 관리

ON 해주고

profile, account_email ON, 설정확인



```html
<a href="{% provider_login_url 'kakao' method='oauth2' %}">카카오로 로그인하기 </a>
```



그런데 일반 로그인을 하면 문제가 발생한다. auth_login에서 문제가 발생하는 것이므로

일단 자동으로 로그인되는 부분을 삭제해 주고 직접 로그인 하도록 바꿔준다.

```python
def profile_update(request):
    try :
        request.user.profile
    except:
        Profile.objects.create(user=request.user)
    ...
```



### 9. 기타 기능들

친구중 친구아닌 사람 3명만 뽑아오기

```python
recommend_users = User.objects.exclude(id__in=request.user.followings.all()).exclude(is_superuser__exact=True).values_list('id', flat=True)
```

values_list는 없어야 그냥 개체가 전달된다.

