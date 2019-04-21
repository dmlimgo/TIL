## Query

pip install ipython # 주피터 노트북 이전에 쓰던 것

0. 모델

   아래 모델을 기반으로 진행

   ```python
   from django.db import models
   
   # Create your models here.
   class User(models.Model):
       name = models.CharField(max_length=20)
       
   class Post(models.Model):
       title = models.CharField(max_length=20)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       
   class Comment(models.Model):
       content = models.CharField(max_length=20)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       post = models.ForeignKey(Post, on_delete=models.CASCADE)
   ```

   

1. 생성

   1.1 사용자 생성

   ```python
   user1 = User.objects.create(name='Kim')
   ```

   다른 방법

   ```python
   user2 = User()
   user2.name = 'Park'
   user2.save()
   ```

   1.2 글 생성

   ```python
   post1 = Post.objects.create(title="1번글", user=user1)
   post2 = Post.objects.create(title="2번글", user=user2)
   post3 = Post.objects.create(title="3번글", user=user1)
   ```

   1.3 댓글생성

   ```python
   c1 = Comment.objects.create(content="1글1댓글", user=user1, post=post1)
   ```

   

2. 쿼리 날리기

   ```python
   # user1이 쓴 댓글들
   user1.comment_set.all()
   # user1이 쓴 글들
   user1.post_set.all()
   ```

   ```python
   >>> Comment.objects.filter(user_id=1)
   <QuerySet [<Comment: Comment object (1)>]>
   ```

   ```python
   # post1의 작성자를 가져와보자
   post1.user
   # post1의 제목을 알아보자
   post1.title
   # post1의 작성자의 이름을 가져와보자
   post1.user.name
   ```

   ```python
   #4. user1이 작성한 모든 댓글의 내용을 출력하는 코드
   {% for comment in user1.comment_set.all %}
   	{{ comment.content }}
   {% endfor %}
   ```

   ```python
   #5. 각각의 게시글마다 댓글을 출력
   {% for post in Post.objects.all %}
   	{% for comment in post.comment_set.all %}
       	{{ comment.content }}
       {% endfor %}
   {% endfor %}
   ```

   ```python
   #6. id가 2인 댓글을 쓴 사람의 게시글들은?
   Comment.objects.get(pk=2).user.post_set.all()
   ```

   ```python
   #7. 1번 글의 댓글들 중 첫번째를 쓴 사람의 이름은?
   Post.objects.get(pk=1).comment_set.first().user.name
   # LIMIT 1 옵션이 적용된 것.
   # all()[0]에서 LIMIT 1이 적용되면서 쿼리가 날아간다.
   Post.objects.get(pk=1).comment_set.all()[0].user.name
   ```

   ```python
   #8. 1번 글의 댓글들 중 2,3,4번을 가지고 온다면?
   # OFFSET 1 LIMIT 3
   Post.objects.get(pk=1).comment_set.all()[1:4]
   ```

   ```python
   #9. 1번 글의 두번째 댓글을 쓴 사람의 첫번째 게시물의 작성자의 이름은?
   Post.objects.get(pk=1).comment_set.all()[1].user.post_set.all()[0].user.name
   ```

   ```python
   # 어디에서 오류가 날까?
   Post.image_set.first.file.url
   Post.image_set -> None
   Post.image_set.first -> None
   Post.image_set.first.file -> AttributeError: Nonetype has no file 뭐 이런식으로.
   ```

   ```python
   # 쿼리가 어떻게 날아갈까?
   >>> print(Post.objects.get(pk=1).comment_set.all()[1:2].query)
   SELECT "onetomany_comment"."id", "onetomany_comment"."content", "onetomany_comment"."user_id", "onetomany_comment"."post_id" FROM "onetomany_comment" WHERE "onetomany_comment"."post_id" = 1  LIMIT 1 OFFSET 1
   ```

   기본적으로 쿼리는 SELECT * FROM comment 형식으로 나감

   하지만 아래는 SELECT user FROM comment로 날림

   ```python
   # 10. SELECT user FROM comment로 쿼리를 날려보자
   # 오브젝트가 아닌 특정한 컬럼의 값을 가지고 오는 경우
   >>> Comment.objects.values('user')
   <QuerySet [{'user': 1}, {'user': 1}, {'user': 1}, {'user': 1}, {'user': 2}, {'user': 2}]>
   
   >>> Comment.objects.values('user', 'post') 
   <QuerySet [{'user': 1, 'post': 1}, {'user': 2, 'post': 1}, {'user': 1, 'post': 1}, {'user': 2, 'post': 2}, {'user': 1, 'post': 3}, {'user': 1, 'post': 2}]>
   ```

   ```python
   # 11. 게시물을 pk값의 내림차순으로 가지고 온다면?
   Post.objects.order_by('-pk') # 내림차순은 '-' 오름차순은 그냥
   ```

   ```python
   # 12. 1글 이라는 제목이 있는 게시글?
   Post.objects.filter(title='1글')
   ```

   ```python
   # 13. 제목에 1이 들어가있는 게시글
   # LIKE %%
   # 대소문자 구분을 해서 가져오겠다.
   Post.objects.filter(title__contains='1')
   # 대소문자 구분을 안하고 가져오겠다.
   Post.objects.filter(title__icontains='1')
   ```

   ```python
   # 14. 댓글들 중에서 해당하는 글의 제목에 1이 들어가는 경우
   Comment.objects.filter(post__title__contains='1')
   ```

   

