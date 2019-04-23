## DJango API

> 190423 강의내용
>
> 영화 정보를 보여주는 API 서버를 만들어보자
>
> django-intro / music_api 프로젝트에서 진행

[TOC]

#### 0. 들어가기전에

###### 0.0 [Restful API](<https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html>)

- 웹의 장점을 최대한 활용할 수 있는 아키텍쳐 스타일

- HTTP METHOD + URI(URL)

- CRUD 는 각각 POST, GET, PUT, DELETE 방식으로 처리한다.





#### 1. 준비

###### 1.1 설치

- Postman 설치(64bit) - 요청을 대신 보내주는 아이

- pip install djangorestframework ( settings.py에 `rest_framework`등록 )

- pip install django-rest-swagger ( settings.py에  `rest_framework_swagger`등록)

###### 1.2 models.py

```python
class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
        
class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    content = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
```

###### 1.3 admin.py

```python
생략
```

후 Artist랑 Music을 몇개 추가해준다.

###### 1.4 urls 설정

```python
urlpatterns = [
    ...
    path('api/v1/', include('musics.urls')),
]
```





#### 2. CRUD

##### 2.1 Read (GET)

###### 2.1.1 음악 전체 목록 출력

`musics/serializers.py` 생성

```python
from rest_framework import serializers

from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist']
```

`views.py` 메소드 선언

```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Music
from .serializers import MusicSerializer

# Create your views here.
# 처리할 메소드 지정
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # context넘겼던 것 처럼 알아서 MusicSerializer가 변환해줌
    # 양이 많으면 many=True 설정해줘야 함
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
```

실행결과

![serailizer_1](image\serailizer_1.PNG)

`Postman`에서 `GET`으로 설정해 주고 `url`란에다 붙여넣고 `Send`를 누르면 내용을 확인할 수 있다.

![serializer_2](image\serializer_2.PNG)



###### 2.1.2 음악 상세 정보

`serializers.py ` 에 메소드 선언

```python
@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
```

결과창 확인

![serializer_3](image\serializer_3.PNG)



###### 2.1.3 아티스트 전체 목록 (1:N 관계 출력)

`serializers.py`에 메소드 선언

```python
class ArtistSerializer(serializers.ModelSerializer):
    # 아래 줄을 추가해줘야 fields에 정상적으로 들어간다.
    music = MusicSerializer(source='music_set', many=True)
    class Meta:
        model = Artist
        fields = '__all__'
```

`views.py`

```python
@api_view(['GET'])
def artist_list(request):
    '''
    아티스트 목록
    '''
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
```





##### 2.2 Create (POST)

###### 2.2.1 댓글 생성하기 

`serializers.py`

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
```

`urls.py`

```python
urlpatterns = [
    ...
    path('musics/<int:music_pk>/comments/', views.comment_create),
]
```

`views.py`

```python
@api_view(['POST'])
def comment_create(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
        return Response(serializer.data)
```

`포스트맨`

![serial_6](C:\Users\student\Desktop\TIL\image\serial_6.PNG)

POST로 변경 (POST는 redirect가 안되므로 '/' 닫아주어야 함)

Body의 form-data에서 KEY, VALUE 입력





##### 2.3 Delete (DELETE)

###### 2.3.1 댓글 삭제하기

`views.py`

```python
@api_view(['DELETE'])
def comment_update_delete(request, music_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({'message': f'{music_pk}의 댓글이 삭제되었습니다.'})
```

`포스트맨`

![serial_7](C:\Users\student\Desktop\TIL\image\serial_7.PNG)

DELETE로 변경해줘야함





##### 2.4 Update (PUT)

`views.py`

delete에서 확장

```python
@api_view(['DELETE', 'PUT'])
def comment_update_delete(request, music_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    else:
        comment.delete()
        return Response({'message': f'{music_pk}의 댓글이 삭제되었습니다.'})
```

PUT으로 변경 KEY, VALUE 입력해주고 Send.

![serial_8](C:\Users\student\Desktop\TIL\image\serial_8.PNG)



#### 3. Swagger 활용

- pip install django-rest-swagger ( settings.py에  `rest_framework_swagger`등록)

##### 3.1 url 설정

`urls.py`

```python
from rest_framework_swagger.views import get_swagger_view

urlpatterns=[
    path('docs/', get_swagger_view(title='음악 정보 API')),
]
```

![serial_4](C:/Users/student/Desktop/TIL/image/serial_4.PNG)

##### 3.2 Document String

```python
def music_list(request):
    '''
    음악 정보 출력
    '''
    # 상세 설명을 위한 Document String, 메서드 밑에 적으면 적용된다.
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
```

swagger에서 볼 수 있다.

![serial_5](C:/Users/student/Desktop/TIL/image/serial_5.PNG)

#### 