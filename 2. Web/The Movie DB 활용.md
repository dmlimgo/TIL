## The Movie DB 활용

#### 1. 준비하기

###### 1.1 API 발급

가입 > 프로필사진 클릭 > 좌측 메뉴 settings > API > create

API Key 발급: 38049eb2ee07785abe8b340e4e1ab965

###### 1.2 포스트맨

포스트맨 열고

Navbar에 API 열고 [developers.themoviedb.org](https://developers.themoviedb.org/3)클릭



#### 2. 요청 보내기

##### 2.1 평점이 가장 높은 영화 찾기

MOVIES탭 > GET Get Top Rated > api_key 입력 > Try it out탭 클릭 > SEND REQUEST 옆의 주소 복사. > 포스트맨에서 SEND



##### 2.2  POST요청으로 영화 평가하기 

###### 2.2.1 Request token 받기

포스트맨으로 해당 URL로 요청 : https://api.themoviedb.org/3/authentication/token/new?api_key=38049eb2ee07785abe8b340e4e1ab965

"request_token" : "604bae6c71bbe9cd236f3aa43513ed4d6483f1b6"

으로 응답이 온다.

![api_1](C:\Users\student\Desktop\TIL\image\api_1.PNG)

###### 2.2.2 인증받기(아닌듯..)

크롬 브라우저에 해당 URL 입력 :<https://www.themoviedb.org/authenticate/604bae6c71bbe9cd236f3aa43513ed4d6483f1b6>

홈페이지로 이동 한 뒤 승인(Approve) 클릭

###### 2.2.3 Authentication

[AUTHENTICATION > Create Session](<https://developers.themoviedb.org/3/authentication/create-session>)

![api_2](C:\Users\student\Desktop\TIL\image\api_2.PNG)

session_id : fd4f1e42f055c1a4944e3387b3f15e630c13f299

###### 2.2.4 평점 남기기

[MOVIES > Rate Movie](<https://developers.themoviedb.org/3/movies/rate-movie>)

![api_4](C:\Users\student\Desktop\TIL\image\api_4.PNG)