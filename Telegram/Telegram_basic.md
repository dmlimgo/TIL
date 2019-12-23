# Telegram



1. 시작하기

   1.1 @BotFather 검색 후 명령어를 입력한다.

   ![telegram1](C:\Users\Lim\Desktop\SSAFY\TIL\8. Picture\telegram1.PNG)

   ```
   /start	
   /newbot
   'bot 이름 지정'
   ```

   1.2 그럼 Token을 주는데 비밀번호와 같으니 반드시 안보이게 보관하자

![telegram2](C:\Users\Lim\Desktop\SSAFY\TIL\8. Picture\telegram2.PNG)

​	1.2.1 환경변수에 Token 저장하기

```powershell
$ vi ~/.bash_profile
$ export TELEGRAM_TOKEN = 'token'
# 이후 import os 모듈을 이용해서 os.getenv('TELEGRAM_TOKEN')메소드를 이용해 접근
```



​	1.3 맨 밑의 링크로 접속하면 다음 단계가 나옴. 아래 주소에 `<token>`자리에 `받은 token`을 복사, `METHOD_NAME`에 `GetMe`라고 입력한다.

```
https://api.telegram.org/bot<token>/METHOD_NAME
```

