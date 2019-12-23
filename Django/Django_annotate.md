## 1. detail 페이지에서 보여주기

* 단일 평균 

```python
from django.db.models import Avg
# 컬럼을 만들어서 한번에 쿼리를 보내는 방식
movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movies_pk)

# 쿼리 여러번 보내는 방식(안 좋음)
movie = Movie.objects.get(pk=movies_pk)
avg_score = movie.score_set.aggregate(Avg('score'))
```

* 대응되는 sql문

```sql
SELECT
"movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description", "movies_movie"."genre_id", AVG("movies_score"."score") AS "score_avg"
FROM "movies_movie" LEFT OUTER JOIN "movies_score" ON ("movies_movie"."id" = "movies_score"."movie_id") WHERE "movies_movie"."id" = '1' GROUP BY "movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description", "movies_movie"."genre_id"
```

* 현재 Score 테이블이 다음과 같다면,
  1. Score

| id   | content      | score | movie_id |
| ---- | ------------ | ----- | -------- |
| 1    | 짱짱         | 10    | 2        |
| 2    | 고양이졸귀탱 | 6     | 1        |
| 3    | 마블 명작    | 8     | 1        |
| 4    | 아 잤네여;;  | 1     | 1        |

movie_id가 1(`.get(pk=)`)이면서, score 테이블의 score 컬럼의(`score__score`) 평균(`Avg`)을 `score_avg` 라는 칼럼으로 추가적으로 붙여서(`annotate`) 결과를 받아보겠다.

* 해당 sql 결과 table은 다음과 같이 작성된다.

| id   | title     | audience | poster_url | description | genre_id | score_avg |
| ---- | --------- | -------- | ---------- | ----------- | -------- | --------- |
| 1    | 캡틴 마블 | 3035808  | Https://   | 캡틴 마블.. | 9        | 5         |







## 2. index에서 보여주기

* 모든 영화에 각각 평균 값

```python
from django.db.models import Avg
movies = Movie.objects.all().annotate(score_avg=Avg('score__score'))
```

* 대응되는 sql문

```sql
SELECT
"movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description", "movies_movie"."genre_id", AVG("movies_score"."score") AS "score_avg"
FROM "movies_movie" LEFT OUTER JOIN "movies_score" ON ("movies_movie"."id" = "movies_score"."movie_id") GROUP BY "movies_movie"."id", "movies_movie"."title", "movies_movie"."audience", "movies_movie"."poster_url", "movies_movie"."description", "movies_movie"."genre_id"
```

- 현재 Score 테이블이 다음과 같다면,
  1. Score

| id   | content      | score | movie_id |
| ---- | ------------ | ----- | -------- |
| 1    | 짱짱         | 10    | 2        |
| 2    | 고양이졸귀탱 | 6     | 1        |
| 3    | 마블 명작    | 8     | 1        |
| 4    | 아 잤네여;;  | 1     | 1        |

score 테이블의 score 컬럼의(`score__score`) 평균(`Avg`)을 `score_avg` 라는 칼럼으로 추가적으로 붙여서(`annotate`) 모든 데이터의 결과를 받아보겠다.

- 해당 sql 결과 table은 다음과 같이 작성된다.

| id   | title             | audience | poster_url | description | genre_id | score_avg |
| ---- | ----------------- | -------- | ---------- | ----------- | -------- | --------- |
| 1    | 캡틴 마블         | 3035808  | Https://   | 캡틴 마블.. | 9        | 5         |
| 2    | 항거:유관순이야기 | 1041939  | Https:..   | ...         | 3        | 10        |
| ...  |                   |          |            |             |          |           |

* 따라서, 템플릿에서 다음과 같이 작성된다.

```jinja2
    {% for movie in movies %}
    	<p><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
    	<p>{{ movie.score_avg }}</p>
    	<img src="{{movie.poster_url}}">
    	<hr>
    {% endfor %}
```

