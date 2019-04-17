## Django Forms



### 1. UserCreationForm

> <https://www.pydanny.com/overloading-form-fields.html>
>
> <https://gist.github.com/rochacon/1514222>

회원가입 폼 커스터마이징

widgets 변수를 수정하는 방식으로는 password가 수정되지 않는다.

따라서 init을 변경해주는 방식으로 가야한다.

```python
from django.contrib.auth.forms import UserCreationForm
# 좋지 않은 방법
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})
            field.label=''
            field.help_text=''
            
        # self.fields['password1'].label = ''
        # self.fields['password1'].help_text = ''
        # self.fields['username'].widget.attrs.update({'placeholder': ''})
        
```

css 적용

<https://stackoverflow.com/questions/5827590/css-styling-in-django-forms>

똑같이 attr에 class에 클래스명을 그대로 넣어주면 된다.

```python
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['myfield'].widget.attrs.update({'class' : 'myfieldclass'})
```

