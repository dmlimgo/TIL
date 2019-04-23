## Django Signal

> 190423 강의내용
>
> [공식문서](<https://docs.djangoproject.com/en/2.2/topics/signals/>)가 부실함 
>
> Instagram App에서 진행?



1. 개요

   모델과 관련된 작업을 할 때 그 이전이나 이후에 어떠한 작업을 하고 싶을 때 사용한다.(Signal을 내부적으로 보낸다)

    ```python
   # 공식문서에서 가져옴
   from django.db.models.signals import pre_save
   from django.dispatch import receiver
   from myapp.models import MyModel
   
   # 'sender'가 'pre_save'저장하기 전에 'receiver'받는다(받아서 밑의 함수가 처리해준다)라고 이해하자.
   # 어떠한 작업이 끝나면 무슨일을 하겠다.
   @receiver(pre_save, sender=MyModel)
   def my_handler(sender, **kwargs):
       ...
    ```

   예를 들어 user_form.save()를 하게 되면

   save를 하면서 signals가 날아가게 된다.

2. signals.py 생성

   > [pre_save](<https://docs.djangoproject.com/en/2.2/ref/signals/#django.db.models.signals.pre_save>)

    ```python	
   from django.db.models.signals import post_save
   from django.dispatch import receiver
   
   from django.conf import settings
   from .models import Profile
   
   #post_save: 저장된 이후에 동작(모든 상황에서 kakao 포함)
   @receiver(post_save, sender=settings.AUTH_USER_MODEL)
   #instance랑 created가 필요하고, 나머지는 **kwarg로 받기는 할게.
   def create_user_profile(instance, created, **kwarg):
       # created는 boolean값이다.
       if created:
           # profile의 unique를 위해 get_or_create를 쓴다.
           Profile.objects.get_or_create(user=instance)
    ```

3. apps.py 수정

   > `templatetags` 같은 것들은 알아서 등록이 되는데 `signals`는 아니라서 `ready`라는 메소드에 따로 설정해 줘야 한다.

    ```python
    ...
    class ...:
        ...
        def ready(self):
            from .signals import create_user_profile
    ```

4. apps.py 등록

   사실은 `INSTALLED_APPS`에 `accounts`말고도 `accounts.apps.AccountsConfig`로 써줘도 된다.

   ```python
   INSTALLED_APPS = [
       ...
       # 'accounts',
       'accounts.apps.AccountsConfig',
       ...
   ]
   ```

5. views.py 수정 (코드에 따라 다름)

   ```python
   def signup(request):
       ...
               # signal가 있기 때문에 아래 코드는 필요없다.
               # Profile.objects.create(user=user)
   ```

