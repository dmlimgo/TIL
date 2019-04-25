## Django validator

```python
from django.db import models
from django.core.validators import MinValueValidator, EmailValidator


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(19, message="미성년는 노노")])
    email = models.CharField(max_length=100, validators=[EmailValidator(message="이메일 형식에 맞지 않습니다.")])
```