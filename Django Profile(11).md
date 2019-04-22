## Django Profile(1:1)

> Instagram Follow 기능 구현
>
> 1:1 구현

![django_3](image\django_3.jpg)

### 1. OneToOneField

models.py

```python
...
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

views.py

```python
def profile_update(request):
    if request.method == 'POST':
        # data=request.FIELS 로 해도 됌 키워드로
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'accounts/profile_update.html', context)
```

다만 superuser는 복잡한 설정을 해줘야하니 일단은 넘어가자..

### 2. 팔로잉

> AbstractUser 설명 <https://whatisthenext.tistory.com/128>

settings.py

```python
AUTH_USER_MODEL = 'accounts.User'
```

이렇게 하는 순간 UserForm에 model을 그냥 auth.models 의 User로 설정해 놓았다면 오류가 난다.

get_user_model()을 이용해서 가져와야 한다.

models.py

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField(
                    settings.AUTH_USER_MODEL, 
                    related_name='followings'
                    )
```

views.py

```python
@login_required
def list(request):
    from django.db.models import Q
    posts = Post.objects.filter(
                        Q(user__in=request.user.followings.values('id'))
                        | Q(user=request.user.id)
                        ).order_by('-pk')
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)
```



### 3. Query 줄이기

> 알아만 두자

#### 3.0 기본코드

```python
from django.db.models import Prefetch
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    context = {'user_info': user}
    return render(request, 'accounts/detail.html', context)
```



#### 3.1 Prefetch

> query를 한번에 다 가져와서 query를 적게 날리자

prefetch_related: 1:N/M:N -> N개를 미리 가져올때(JOIN table)

select_related: 1:N -> 1개를 미리 가져올 때(JOIN)

```python
from django.db.models import Prefetch
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    followings = user.followings.prefetch_related(
                                            Prefetch('score_set',
                                            queryset=Score.objects.select_related('movie').order_by('-value'),
                                            to_attr='score_set_value_order'
                                            ))
    context = {'user_info': user}
    return render(request, 'accounts/detail.html', context)
```

```html
# 이 코드를
{{ user_follow.score_set.first.movie.title }}
{{ user_follow.score_set.first.value }}
# 아래처럼 쓸 수 있다.
# first는 queryset에서만 쓸 수 있으므로 0을 써줘야 한다.
{{ user_follow.score_set_value_order.0.movie.title }}
{{ user_follow.score_set_value_order.0.value }}
```



#### 3.2 Annotate

> query를 줄여보자
>
> 2개를 1개로 아낄 수 있음

Column을 추가해서 값을 넣어놓는 것

```python
from django.db.models import Prefetch
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User.objects.annotate(
        						followers_count=Count('followers'),
        						followings_count=Count('followings')
    							), pk=user_pk)
    context = {'user_info': user}
    return render(request, 'accounts/detail.html', context)
```

```html
{{ user_info.followings.count }}
{{ user_info.followers.count}}
# 아래 코드처럼 쓸 수 있다.
{{ user_info.followings_count }}
{{ user_info.followers_count }}
```

