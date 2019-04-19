## 09 Project

1. accounts App
     1. 유저 목록 ( accounts/ )
        - 사용자의 목록 출력, 상세페이지 링크 설정
        - gravatar 프로필사진 활용
     2. 유저 상세보기 ( accounts/{user_pk}/ )
        - follow, unfollow구현, 해당 유저가 작성한 평점 정보 출력, 팔로워수/팔로잉수 출력
        - 팔로우, 팔로잉 사람 수를 클릭하면 사람들 목록이 출력

2. movies App
   1. 영화 목록
      - 영화 상세보기 페이지 구현
   2. 영화 상세보기
      - 관련정보나열, 로그인 한 사람만 평점 남기기, 모든사람 평점 목록 열람가능
   3. 평점 생성
      - login_required, POST방식, 동적할당, 페이지 redirect