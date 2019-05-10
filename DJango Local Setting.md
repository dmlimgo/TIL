# DJango Local Setting

> 0510 강의내용

[pyenv github](<https://github.com/pyenv/pyenv>)

[pyenv-win github](<https://github.com/pyenv-win/pyenv-win>)

gitbash에 아래 명령어 입력

```bash
pip install pyenv-win --target $HOME/.pyenv
```

환경변수 > 위에 창에 Path > 편집 

```
C:\Users\student\.pyenv\pyenv-win\shims
C:\Users\student\.pyenv\pyenv-win\bin
```

pyenv치면 정보가 뜬다. 업데이트 해주자. 파이썬도 업데이트된다.

Disable도 해주자

```bash
pyenv install 3.6.8
```

아래 명령어로 버전 확인

```bash
pyenv versions
```

bash_profile에 아래 내용 복사.

```bash
export PATH="/c/Users/student/.pyenv/bin:$PATH"
```

***시스템 변수의 Path에 python 경로 설정이 되어있다면 지워준다.

```bash
python -V
```

---

이후

```bash
pyenv install 3.7.2
pyenv global 3.7.2
pyenv rehash
python -V
===가상환경 원하는 폴더에서===
python -m venv django-venv
cd django-venv
source Scripts/activate
===그러면 이렇게 될 것 ===
(django-venv)student@DESKTOP MINGW64 ~/Desktop/django/django-venv
```

한다. git 쓰기 좋아서 3.7버전씀