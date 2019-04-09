# Django_login

> 190408 로그인 화면 만들기 시작



### 0. 준비사항

###### 0.0 shell_plus

> 꼭 필요한건 아님. 입/출력 확인을 위한 도구.

`shell_plus`를 이용하기 위해 `django_extenstions`이 pip install해야 한다.

`settings.py`의 `INSTALLED_APPS`에 `django_extensions`가 있는지 확인

###### 0.1 HTTP

> HTTP의 가장 큰 특징 `connectless`, `stateless`
>
> `connectless` : 요청, 응답만 해주고 끝.
>
> `stateless`: 상태를 저장해 두지 않음. NAVER API를 이용해 크롤링 할 때 NAVER_ID와 SECRET로 계속 요청을 보내줘야 하는 이유.

![django_login_2](C:\Users\student\Desktop\TIL\image\django_login_2.jpg)

쿠팡 등에서 장바구니에 담으면 `쿠키`(크롬의 경우 자물쇠를 클릭해서 나오는 곳)에 담긴다. HTTP가 상태를 저장하지 않기 때문에 사용자의 브라우저(클라이언트)에 저장하는 것.

`쿠키`와 같이 나오는 개념이 `세션`이라는게 있다.

크롬의 `사용 중인 쿠키`를 보면 `로컬 저장소`, `세션 저장소`, `쿠키`가 있는데

`쿠키`의 경우 클라이언트에만 저장을 해서 클라이언트에서 받아서 표시?를 하는데

`세션`은 클라이언트와 서버에 같이 저장한다. 서버에서 쿠키의 정보가 서버의 정보가 일치하는지 검증한다.



### 1. 시작하기

#### 1.1 유저 확인하기

관리자를 생성한다.

```bash
python manage.py createsuperuser
```

메소드들을 확인하기 위해 shell 접근.

```bash
python manage.py shell_plus
```

알아서 유저와 모델들을 import 해준다.

```bash
from boards.model import Board
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth import get_user_model
...
```

아래 명령어를 입력하여 createsuperuser로 생성한 계정의 QuerySet을 확인할 수 있다.

```bash
>> User.objects.all()
<QuerySet [<User: dong>]>
```

위에 import 되어 있기 때문에 아래 처럼 가져올 수도 있다.

```bash
>> Uuser = get_user_model() #User 오브젝트 자체를 리턴
>> Uuser.objects.all()
<QuerySet [<User: dong>]>
```



#### 1.2. User 메소드

###### 1.2.1 <i>object</i>.last_name, first_name

```bash
>>> u = User.objects.all()[0] # 여기서는 Superuser가 0번째이다
>>> u.last_name = 'Kim'
>>> u.first_name = 'Seulgi'
>>> u.save()
```

###### 1.2.2 <i>object</i>.get_full_name()

```bash
>>> u.get_full_name()
'Seulki kim'
```

###### 1.2.3 <i>object</i>.password

```bash
>>> u.password
'pbkdf2_sha256$120000$2VzzwFWTHprB$c9StBvq7Azg65lxFtYHDKvUlw8qoRmm5xdpgWUUYGHA='
```

###### 1.2.4 <i>Class</i>.objects.create_user(<i>'value1', 'value2', 'value3', ...</i>)

> 새로운 User를 만들어주는 메소드.

```bash
>>> u = User.objects.create_user('name', 'email', 'password')
```

###### 1.2.5 <i>object</i>.check_password(<i>'str'</i>)

> 입력한 비밀번호가 암호화 되어 있는지 확인하는 메소드. True와 False를 리턴한다.

```bash
>>> u = User.objects.create_user('seulki', 'a@g.c', '123')
>>> u.check_password('123')
True
```

###### 1.2.6 <i>object</i>.set_password(<i>'str'</i>)

> `PBKDF2`를 사용하여 입력한 비밀번호를 암호화 해 저장한다. `django.contrib.auth`에서 해당 내용을 처리한다. 해시알고리즘과 SHA256이 연관되어 있는거 같다.

`password`변수를 직접 변경하면 `check_password` 메소드로 False가 출력되니 주의하자. 

```bash
>>> u.password = '123'
>>> u.check_password('123')
False
```

`set_password` 메소드를 이용하여 설정해 줄 수 있다.

```bash
>>> u.set_password('123')
>>> u.check_password('123')
True
```



### 2. Django.contrib.auth 사용하기

> <https://docs.djangoproject.com/en/2.2/topics/auth/default/>

###### 2.0 준비하기

왜 이거 쓰더라...

```python
# settings.py
INSTALLED_APPS = [
	...
    'crispy_forms',
    ...
]
```

로그인 후 어디로 갈지 정해줄 수 있다. 

@login_required랑 차이가 뭐더라.

```python
# settings.py
LOGIN_URL = '/boards/'
```







###### 2.1 settings.py

###### 2.2 urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

###### 2.3.1 accounts/views.py

```python
import pprint
from django.shortcuts import render, redirect
# 유저와 관련된 것은 다 auth에서 진행
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    # request로 뭐가 넘어오는지 확인해보자
    # pprint.pprint(dir(request))
    # 아래 두 줄 만으로 주소창을 이용해 기어들어오는 것을 막을 수 있다.
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        user_form = UserCreationForm()
    context = {'user_form': user_form}
    return render(request, 'accounts/signup.html', context)
```

```python
# def와 피하기 위해 as를 사용함
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            # db에 저장 하는게 아니기 때문에 form.save()하지 않음
            auth_login(request, login_form.get_user())
            # session을 만들기 위해 함수를 쓴다. request 정보를 넘겨줘야 한다는 걸 기억하자.
            return redirect('boards:index')
    else:
        login_form = AuthenticationForm()
    context = {'login_form': AuthenticationForm()}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('boards:index')
```

###### 2.3.2 boards/views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Board
from .forms import BoardForm

@login_required
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

@login_required
def create(request):
    # if not request.user.is_authenticated:
        # return redirect('boards:index')
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            # title = board_form.cleaned_data.get('title')
            # content = board_form.cleaned_data.get('content')
            # board = Board(title=title, content=content)
            # board.save()
            board = board_form.save()
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {'board_form': board_form}
    return render(request, 'boards/form.html', context)
```

###### 2.4 forms.py

```python
from django import forms
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ['username', 'password']
```

###### 2.5 signup.html



{{ user }} 태그로 사용자의 정보를 나타낼 수 있다.



지금까지는 context로 정보를 넘겨서 표시했지만

user는 request에서 request.user로 정보를 가져오기 때문에 그냥 써도 된다.





---

새로운 워크스페이스 생성할 때

당분간 Django가 안정화 될 때까지

2.1.5 버전을 설치해서 쓰자

```bash
pip install django==2.1.5
```

---





---

from django.contrib.auth.decorators import login_required

해놓고 @login_required 같이 가는 코드





`settings.py`에 `LOGIN_URL`을 선언해 로그인 후 어디로 갈지 정해줄 수 있다.

login_required는 자동적으로 사용자가 원래 접근했던 페이지 주소를 가지고 로그인 후 바로 연결해주는 기능을 가지고 있다.





http 요청을 받을지 말지 처리해주는 데코레이터

@require_http_methods(["GET", "POST"])



USER DELETE

USER CHANGEFORM



비밀번호 수정하기



글쓴이 출력하기 settings.AUTH_USER_MODEL