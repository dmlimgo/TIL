# VueDjango

> 0509 강의내용
>
> music_api앱으로 요청을 보내보자.

(참고) vue-resource란게 있는데 이거 쓰지말고 axios쓰자.



music_api앱의 `/api/v1/musics/`에 요청을 보내 음악 목록을 받아보자.

```html
<body>
    <div id="app">
        <ul>
            <li v-for=""></li>
        </ul>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                musics: []
            },
            methods: {
                getMusics: function() {
                    axios.get('http://django-intro-dmlim.c9users.io:8080/api/v1/musics/')
                        .then(response => {
                            console.log(response)
                        })
                        .catch(error => {
                            console.log(error)
                        })
                }
            }
        })
    </script>
</body>
```

위와 같이 작성하고 `getMusics`메서드로 요청을 보내면(재주껏) CORS오류가 뜬다.

CORS오류란 script 태그 내에서 다른 호스트로 요청을 보내는 것이 기본적으로 금지되어 있다. 이것이 CORS 정책이다.

요청이 실패하면 `.then`이 아니라 `.catch`가 실행되기 때문에 오류를 자세히 보기위해 사용해보자.

오류를 보면 CORS에 의해 요청이 거절되었다고 더 정확하게 나온다.

Django로 돌아가서 `django-cors-headers`를 설치해주자.

[cors github](<https://github.com/ottoyiu/django-cors-headers>)

```bash
$ pip install django-cors-headers
```

설치 후 Django의 `INSTALLED_APPS`에 `corsheaders`를 추가,

`MIDDLEWARE`에 `corsheaders.middleware.CorsMiddleware`를 추가해주는데 문서에 보면 정확한 위치가 나와있다(원래 있는 것?을 써준걸 보면). 보통 이렇게 굳이 이렇게 위치를 지정해주면 따라줘야 한다.

공식문서의 Configures를 보면 `ALLOW_ALL` 할거냐 `WHITELIST`를 쓸거냐 물어보는데 

모두에게 허용할거면 `ALLOW ALL`, 특정된 곳에만 허용할거면 `WHITELIST`를 쓴다.

 빈 공간에 추가

```python
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'localhost:8000',
    'naver.com'
]
```

다시 요청해보자

```html
<body>
    <div id="app">
        <!-- <button @click="getMusics">가져오기</button> -->
        <ul>
            <li v-for="music in musics">{{ music.title }}</li>
        </ul>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                musics: []
            },
            mounted: function() {
                axios.get('http://django-intro-dmlim.c9users.io:8080/api/v1/musics/')
                    .then(response => {
                        console.log(response)
                        this.musics = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            methods: {
                
            }
        })
    </script>
</body>
```

`mounted`를 사용해서 페이지 로딩이 끝나는 즉시 실행되게 하자.

{{ music.artist }}가 id값으로 나올텐데

django의 `serializers.py`에 artist_name을 따로 추가해주자

```python
class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'artist_name']
```

```html
<div id="app">
    <ul>
        <li v-for="music in musics">{{ music.artist_name }} | {{ music.title }}</li>
    </ul>
</div>
```

위처럼 사용하면 된다.

`comment_set`을 표시해보자.

```html
<div id="app">
    <ul>
        <li v-for="music in musics">
            {{ music.artist_name }} | {{ music.title }}<br>                
            <ul>
                <li v-for="comment in music.comment_set">
                    {{ comment.content }}
                </li>
            </ul>
        </li>
    </ul>
</div>
```

---

크롬 확장프로그램에서 `vue.js devtools`를 다운받자.

생성된 아이콘에서 우클릭 > 확장프로그램 > 파일 URL에 대한 액세스 허용을 파란색으로 바꿔주자.

그럼 Console 창있는곳에 Vue가 추가되어 있고 데이터가 뭐가 있는지 알려준다.

---

댓글을 달아보자

```html
<div id="app">
    <ul>
        <li v-for="music in musics">
            {{ music.artist_name }} | {{ music.title }}<br>
            <input v-model="newComment">               
            <ul>
                <li v-for="comment in music.comment_set">
                    {{ comment.content }}
                </li>
            </ul>
            <hr>
        </li>
    </ul>
</div>
```

일단 input창을 써주고, v-model로 연결해준다.

그런데 이렇게 하면 모든 음악의 댓글창에 동시에 연결된다.

그러므로 axios로 받아올 때 각각의 music개체에 댓글 배열을 생성해준다.

{...music, newComment: ''}는 기존의 music을 쭉 펼쳐놓고, newComment를 새로 추가한다는 뜻이다.

```js
mounted: function() {
    axios.get('http://django-intro-dmlim.c9users.io:8080/api/v1/musics/')
        .then(response => {
        this.musics = response.data.map((music) => {
            return {...music, newComment: ''}
        })
    })
        .catch(error => {
        console.log(error)
    })
},
```

```html
<div id="app">
    <ul>
        <li v-for="music in musics">
            {{ music.artist_name }} | {{ music.title }}<br>
            <input v-model="music.newComment" v-on:keyup.enter="createComment(music)">
            <ul>
                <li v-for="comment in music.comment_set">
                    {{ comment.content }}
                </li>
            </ul>
            <hr>
        </li>
    </ul>
</div>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            musics: [],
            newComment: '',
        },
        mounted: function() {
            axios.get('http://django-intro-dmlim.c9users.io:8080/api/v1/musics/')
                .then(response => {
                this.musics = response.data.map((music) => {
                    return {...music, newComment: ''}
                })
            })
                .catch(error => {
                console.log(error)
            })
        },
        methods: {
            createComment: function(music) {
                console.log(music)
                const data = {content: music.newComment}
                axios.post(`http://django-intro-dmlim.c9users.io:8080/api/v1/musics/${music.id}/comments/`, data)
                    .then(response => {
                    console.log(response)
                    music.newComment = ''
                })
                    .catch( error => console.log(error))
            }
        }
    })
</script>
```

하면 올라가긴 한다. 하지만 바로 업데이트가 안된다.

comment_set에 바로 push를 해주면 업데이트가 된다.

```js
axios.post(`http://django-intro-dmlim.c9users.io:8080/api/v1/musics/${music.id}/comments/`, data)
    .then(response => {
    console.log(response)
    music.comment_set.push(response.data)
    music.newComment = ''
})
```

