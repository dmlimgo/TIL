# Js_axios

> 요청을 보내주는 아이



## 설정하기

- [axios.github](<https://github.com/axios/axios>)

```html
<body>
    ...
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</body>
```

##### 1.2.1 axios.get

> [dogAPI](https://dog.ceo/api/) 사용

- 응답 출력

  ```js
  axios.get('https://dog.ceo/api/breeds/image/random')
  .then(response => console.log(response))
  ```

- url 출력

  ```js
  const dogImageUrl = axios.get('https://dog.ceo/api/breeds/image/random')
              .then(response => response.data.message)
              .then(url => console.log(1))
          console.log(2)
          console.log(dogImageUrl)
          console.log(3)
  ----------------------------
  2
  Promise{<pending>}
  3
  1
  ```

  ==응답 순서==가 다름을 알 수 있다. 

  Promise{<pending>}는 요청을 보내놓고 기다린다는 뜻이다. 하지만 스크립트는 계속 진행되기 때문에 뒤의 명령어들이 실행되고 요청에 대한 응답이 돌아왔을 때  응답이후의 명령어가 실행된다.

- 강아지 표시하기

  ```js
  <body>
  	<h1>댕댕이</h1>
      <div id="animals"></div>
  
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
      <script>
          const getDogImage = function() {
              axios.get('https://dog.ceo/api/breeds/image/random')
                  .then(response => response.data.message)
                  .then(url => {
                  const imageTag = document.createElement('img')
                  imageTag.src = url
                  const animal = document.querySelector('#animals')
                  animal.append(imageTag)
              })
          }
      </script>
  </body>
  ```

- 버튼 눌러서 강아지 표시하기 problem

  ```js
  const getDogImage = function() {
      axios.get('https://dog.ceo/api/breeds/image/random')
          .then(response => response.data.message)
          .then(url => {
          const imageTag = document.createElement('img')
          imageTag.src = url
          const animal = document.querySelector('#animals')
          animal.append(imageTag)
      })
  }
  const dogButton = document.querySelector('#dog')
  dogButton.addEventListener('click', getDogImage)
  ```

- 검색하면 XMLHttpRequests로 실시간으로 검색어에 대한 결과를 나타내주는 것을 알 수 있다.

  ![js_3](C:\Users\student\Desktop\TIL\image\js_3.PNG)

- http://latentflip.com/loupe 



### 2. 좋아요 누르기 실습

- cards

  if 문을 이렇게 하나의 문장으로 바꿔주자

  ```html
  <span class="nav-icon {% if user in post.like_users.all %} cc2nhf {% else %} cc2nh {% endif %}"></span>
  ```

- html

  ```html
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  {% block script %}
  {% endblock %}
  ```

- class를 지정해주자

  ```html
  <span class="nav-icon {% if user in post.like_users.all %} cc2nhf {% else %} cc2nh {% endif %} like-button"></span>
  ```

  ```js
  const likeButtons = document.querySelectorAll('.like-button')
      likeButtons.forEach(function(button) {
          button.addEventListener('click', function(e){
              const postId = e.target.dataset.id
              axios.get(`/posts/${postId}/like/`) 
          })
      })
  ```

  대상이 하나만 있을 경우

  ```js
  const followButton = document.querySelector('.follow-button')
  followButton.addEventListener('click', function(e){
    
  })
  ```

  

  다음과 같이 data-id, data-text 등을 사용하면 dataset으로 묶여서 관리하기가 편해진다.

  ```html
  <span data-id="{{post.pk}}" data-text="하트 클릭" class="nav-icon {% if user in post.like_users.all %} cc2nhf {% else %} cc2nh {% endif %} like-button"></span>
  ```

  ```js
  const likeButtons = document.querySelectorAll('.like-button')
  likeButtons.forEach(function(button) {
      button.addEventListener('click', function(e){
          const postId = e.target.dataset.id
          console.log(postId)
          axios.get(`/posts/${postId}/like/`)
              .then(function(response){
              console.log(response)
          })
      })
  })
  ```

- views.py

  요청을 보내준...다...?

  ```python
  from django.http import JsonResponse
  def like(request, posts_pk):
      ...
      if post.like_users.filter(pk=user.id).exists():
          post.like_users.remove(user)
          is_like = False # JsonResponse에 값을 넘겨주기 위한 값
      else:
          post.like_users.add(user)
          is_like = True
      return JsonResponse({'is_like': is_like})
  ```

- html

  ```js
  const likeButtons = document.querySelectorAll('.like-button')
  likeButtons.forEach(function(button) {
      button.addEventListener('click', function(e){
          const postId = e.target.dataset.id
          console.log(postId)
          axios.get(`/posts/${postId}/like/`)
              .then(function(response){
              console.log(response)
  
              if (response.data.is_like){
                  e.target.classList.remove('cc2nh')
                  e.target.classList.add('cc2nhf')
              } else {
                  e.target.classList.remove('cc2nhf')
                  e.target.classList.add('cc2nh')
              }
          })
      })
  })
  ```

- a tag의 경우 다른 곳으로 요청을 보내기 때문에 그걸 없애주기 위해 아래를 추가해준다.

  ```js
  e.preventDefault()
  ```

- 좋아요 숫자 갱신하기

  count 추가

  views.py

  ```python
  def like(request, posts_pk):
      ...
      return JsonResponse({'is_like': is_like, 'count': post.like_users.count()})
  ```

  html

  ```js
  좋아요<span id="like-count-{{post.pk}}">&nbsp{{ post.like_users.all.count }}</span>개
  
  <script>
  const likeButtons = document.querySelectorAll('.like-button')
  likeButtons.forEach(function(button) {
      button.addEventListener('click', function(e){
          e.preventDefault()
          const postId = e.target.dataset.id
          // console.log(postId)
          axios.get(`/posts/${postId}/like/`)
              .then(function(response){
              // console.log(response)
              const likeCount = document.querySelector(`#like-count-${postId}`)
              likeCount.innerText = response.data.count
              if (response.data.is_like){
                  e.target.classList.remove('cc2nh')
                  e.target.classList.add('cc2nhf')
              } else {
                  e.target.classList.remove('cc2nhf')
                  e.target.classList.add('cc2nh')
              }
          })
      })
  })
  </script>
  
  ```

- axios.post로 보내기

  - axios의 설정에 csrf token을 추가해줘야 한다.

  - [관련글](<https://cbuelter.wordpress.com/2017/04/10/django-csrf-with-axios/>)

    ```js
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    ```

- href 살려두고 href로 요청하기

  ```js
  const url = event.target.getAttribute('href')
  axios.post(url)
  ```

- ajax 요청만 받기

  ```python
  if request.is_ajax():
      ...
      return JsonResponse(data)
  else:
      return HttpResponseBadRequest
  ```

  ```js
  axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
  ```



### 3. 댓글 달기 실습

<https://www.zerocho.com/category/HTML&DOM/post/59465380f2c7fb0018a1a263>



