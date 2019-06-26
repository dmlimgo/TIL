## DJango TestCode & API

> 190423 강의내용
>
> <https://docs.djangoproject.com/en/2.2/intro/tutorial05/#further-testing>



0. 시작하기 전에

   TDD : Test Drive Development

   미리 테스트를 위한 코드를 작성하고 실제 개발을 하자는 내용.

   파이썬은 이런식으로 테스트코드를 작성하는구나, CRUD하면서 이런 것들을 조심했었지 하는 느낌으로 가자.

   

   **Given When Then**

   - testcode를 작성할때 필요한 기본 구조
   - 각각의 구조 밑줄의 내용이 요소이다. 

   ```python
   class BoardViewCreateTest(TestCase):
       def setUp(self):
           # Given
           user = self.make_user(username='test', password='xptmxm!')
       
       def test_01_get(self):
           # When
           with self.login(username='test', password='xptmxm!'):
               response = self.get_check_200('boards:create')
               # Then
               self.assertIsInstance(response.context['form'], BoardForm)
   ```

   

1. 준비

   `testcode`를 더 간결하게 작성할 수 있게 도와준다.

   ```bash
   $ pip install django_test_plus
   ```

   선생님 코드 clone

   ```bash
   $ git clone https://lab.ssafy.com/edutak/django_test.git
   ```

   Migrate

   ```bash
   생략
   ```

2. Test.py

   1. settings.py

      ```python
      # tests.py
      # 0423 DJango TestCode & API 내용
      from test_plus.test import TestCase
      
      from django.conf import settings
      # class이름은 상관없음
      class SettingsTest(TestCase):
          # 메서드는 반드시 test로 시작해야함
          def test_01_settings_locale(self):
              self.assertEqual(settings.USE_I18N, True)
              self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
      ```

      작성 후 bash에서 명령어 입력

      ```bash
      $ python manage.py test boards
      ```

      결과에 따라 성공시

       ```bash
       .
       -----------------------------------------------------------
       Ran 1 test in 0.001s
       OK
       ```

      실패시

       ```bash
       F
       ======================================================================
       FAIL: test_01_settings_locale (boards.tests.SettingsTest)
       ```

      와 같이 출력된다.

   2. models.py

      ```python
      class BoardModelTest(TestCase):
          def test_01_model(self):
              board = Board.objects.create(title="제목테스트",
                                  content="내용",
                                  user_id=1)
              self.assertEqual(str(board), f'Board{board.pk}')
      ```

      가상 DB에 저장되었다가 알아서 없어진다.

   3. CRUD - Create

      ```python
      from .forms import BoardForm
      class BoardViewCreateTest(TestCase):
          def test_01_get(self):
              response = self.get_check_200('boards:create')
              # 응답의 시작에 '<form'태그가 포함되어 있느냐
              # self.assertContains(response, '<form')
              # 위에거 안돌아감 왜인지 설명 x
              
              # form이 BoardForm이냐
              self.assertIsInstance(response.context['form'], BoardForm)
      ```

      302에러가 뜬다. -> 로그인 안하고 글을 썼을 때 오류가 나게 설정해 뒀었음(코드에)

      로그인을 시켜준다.

      ```python
      from .forms import BoardForm
      class BoardViewCreateTest(TestCase):
          def test_01_get(self):
              user = self.make_user(username='test', password='xptmxm!')
              # with 다음 문장을 실행하고 with가 끝나면 다시 없앤다(logout)
              with self.login(username='test', password='xptmxm!'):
                  response = self.get_check_200('boards:create')
      
                  # form이 BoardForm이냐
                  self.assertIsInstance(response.context['form'], BoardForm)
      ```

      form이 title, content를 가지고 있는지 점검해보자

      ```python
      class BoardModelTest(TestCase):
          ...
          def test_02_modelform_with_data(self):
              data = {'title': 'test', 'content': 'test'}
              self.assertEqual(BoardForm(data).is_valid(), True)    
          def test_03_modelform_without_title(self):
              data = {'content': 'test'}
              self.assertEqual(BoardForm(data).is_valid(), False)
          def test_04_modelform_without_content(self):
              data = {'title': 'test'}
              self.assertEqual(BoardForm(data).is_valid(), False)
      ```

      공통적으로 실행되어야 하는 코드가 있으면 setUp메소드를 이용한다.

      ```python
      class ...(TestCase):
          def setUp(self):
              # 사용할 때는 self.user로 사용한다.
              user = self.make_user(username='test', password='xptmxm!')
      ```

      뭐라고 하셨는지 모르지만 코드를 보고 이해하자.

      ```python
      class ~(TestCase):
          def test_03_post_redirect_302(self):
              # given
              data = {'title': '제목 작성함', 'content': '냉무'}
              # when
              with self.login(username='test', password='xptmxm!'):
                  self.post('boards:create', data=data)
                  # then
                  self.response_302()
      ```

      

   4. CRUD - Detail

      게시글이 생성되는지 확인

      ```python
      class BoardViewDetailTest(TestCase):
          def setUp(self):
              self.user = self.make_user(username='test', password='xptmxm!')
              self.board = Board.objects.create(
                                      title='제목',
                                      content='내용',
                                      user=self.user
                                      )
          def test_01_get(self):
              self.get_check_200('boards:detail', board_pk=self.board.pk)
      ```

      응답 내용에 title과 content가 있는지 점검.

      ```python
      class ~(TestCase):
          def test_02_contain_board(self):
              self.get_check_200('boards:detail', board_pk=self.board.pk)
              self.assertResponseContains(self.board.title, html=False)
              self.assertResponseContains(self.board.content, html=False)
              # html True False는 html로 볼것이냐 string으로 볼것이냐 차이, 공백을 없애냐, 안없애냐 차이
      ```

      ```python
      class ~(TestCase):
          def test_03_template(self):
              response = self.get_check_200('boards:detail', board_pk=self.board.pk)
              self.assertTemplateUsed(response, 'boards/detail.html')
      ```

   5. CRUD - Delete

      정리 거의 안함 여기부터 그냥 코드 읽고 해석하자 그렇게 어렵진 않을듯.

      ```python
      class BoardViewIndexTest(TestCase):
          def setUp(self):
              self.user = self.make_user(username='test', password='xptmxm!')
              self.board = Board.objects.create(
                                      title='제목',
                                      content='내용',
                                      user=self.user
                                      )
      ```

      ```python
          def test_01_boards_queryset(self):
              self.board = Board.objects.create(
                                      title='제목',
                                      content='내용',
                                      user=self.user
                                      )
              # boards = Board.objects.all()
              boards = Board.objects.order_by('-pk')
              response = self.get_check_200('boards:index')
              self.assertQuerysetEqual(response.context['boards'], map(repr, boards))
      ```

      ```python
        	def test_02_template(self):
              # when
              response = self.get_check_200('boards:index')
              # then
              self.assertTemplateUsed(response, 'boards/index.html')
      ```

      ```python
          def test_03_delete(self):
              with self.login(username='test', password='xptmxm!'):
                  self.post('boards:delete', board_pk=self.board.pk)
                  self.assertEqual(Board.objects.all().count(), 0)
      ```

   6. CRUD - Update

      ```python
      class BoardViewUpdateTest(TestCase):
          def setUp(self):
              # given
              self.user = self.make_user(username='test', password='xptmxm!')
              self.board = Board.objects.create(
                                      title='제목',
                                      content='내용',
                                      user=self.user
                                      )
          
          def test_01_boardform_instance(self):
              with self.login(username='test', password='xptmxm!'):
                  response = self.get_check_200('boards:update', board_pk=self.board.pk)
                  self.assertEqual(response.context['form'].instance.pk, self.board.pk)
      ```

      