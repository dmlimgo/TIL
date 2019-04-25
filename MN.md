## M:N

models.py

```python
...
class Doctor(models.Model):
    name = models.CharField(max_length=10)
    
class Patient(models.Model):
    name = models.CharField(max_length=10)
    # Doctor에 해줘도 됌.
    # related_name은 역참조.
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    
# 중개 모델(Intermediary Model)
# related_name을 선언한 순간 없어도 된다.
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

1. 객체 생성하기

```python
doctor1 = Doctor.objects.create(name='Kim')
doctor2 = Doctor.objects.create(name='Park')
patient1 = Patient.objects.create(name='Tom')
patient2 = Patient.objects.create(name='John')
Reservation.objects.create(doctor=doctor1, patient=patient1)
Reservation.objects.create(doctor=doctor1, patient=patient2)
```

```python
#1 doctor1이 patient1의 정보를 가져온다?
rs = doctor1.reservation_set.all()
for r in rs:
    print(r.patient.name)
```

```python
#2. doctor1의 예약 목록
doctor = Doctor.objects.get(pk=1)
doctor.reservation_set.all()
# 다른 방법
# Reservation.objects.filter(doctor=doctor)
```

```python
#3. doctor1의 환자의 이름
r =  Doctor.objects.get(pk=1).reservation_set.all()
for r in reservations:
    print(r.patient.name)
```

```python
# related_name을 선언함으로써 Doctor클래스에서도 patients를 parameter로 쓸 수 있다.
# 이걸 역참조라고 한다.
doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

>>> Doctor.objects.get(pk=1).patients.all()
<QuerySet [<Patient: Patient object (1)>, <Patient: Patient object (2)>]>
```

중개 모델 없애기

```python
# related_name 넣어주고, 중개모델 삭제한 후
>>> doctor1.patients.add(patient1)
>>> patient2.doctors.add(doctor1)
>>> doctor1.patients.all()
<QuerySet [<Patient: Patient object (1)>, <Patient: Patient object (2)>]>
```

```python
sqlite3에서 .tables를 이용해 확인해 보면
manytomany_patient_doctors
와 같이 테이블이 생성된 것을 볼 수 있다.
```

하지만 저장할 데이터가 많은 경우엔 중개모델이 필요하다

```python
class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    time = models.IntegerField()
```

```python
# ===================================
# 선생님 정리
# 1. Patient에 doctors = ManyToManyField(Doctor, through='Reservation')
patient = Patient.objects.get(pk=1)
patient.doctors.all()
doctor = Doctor.objects.get(pk=1)
doctor.patient_set.all()

# 2. Patient에 doctors = ManyToManyField(Doctor, through='Reservation', related_name='patients')
# 역참조와 관련된 설정을 한다면
patient = Patient.objects.get(pk=1)
patient.doctors.all()
doctor = Doctor.objects.get(pk=1)
doctor.patients.all()

# 3. 예약을 생성한다면
Reservation(patient=patient, doctor=doctor)
#====================================
```

* 중계모델이 없는 상태로 ManyToManyField를 사용하면 db에 column이 생기는게 아니라 중계모델이 생겨서 각각의 id값을 저장한다.

#### 2. 응용

인스타 그램 좋아요 적용하기

models.py

```python
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user.post_set.all() - 게시글인지? 좋아요한 글인지? 알수없다
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # 따라서 related_name을 추가해 헷갈리지 않게 해준다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    # image = models.ImageField()
```

views.py

```python
def like(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    user = request.user
    # user가 지금 해당 게시글에 좋아요를 한 적이 있는지?
    # if user in post.like_users.all():
    #     post.like_users.remove(user)
    # else:
    #     post.like_users.add(user)
    if post.like_users.filter(pk=user.id).exists():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:list')
```

html

```html
{% if user in post.like_users.all %}
	<a href="{% url 'posts:like' post.pk %}"><i class="fas fa-heart fa-1.5x" style="color:crimson"></i></a>
{% else %}
	<a href="{% url 'posts:like' post.pk %}"><i class="far fa-heart fa-1.5x" style="color:darkgray"></i></a>
{% endif %}
<span>{{ post.like_count }}명이 좋아요를 눌렀습니다.</span>
```

추가

models.py

함수를 만들어 사용할 수도 있다.

```python
class Post(models.Model):
	...
    @property
    def like_count(self):
        return self.like_users.count()
    ...
```

```html
{{ post.like_count }}
```

???

```html
{% url 'posts:like' post.pk %}?next={% url 'posts:list' %}

{% url 'posts:like' post.pk %}?next={% url 'posts:%}

return redirect(request.GET.get('next') or (
'posts:detail', post_pk))
```

