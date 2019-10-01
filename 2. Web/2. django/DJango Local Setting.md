# DJango Local Setting

> 0510 강의내용
>
> 0930 전체적으로 수정

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

gitbash를 다시 열어주고 아래 명령어로 버전을 확인해준다.

```bash
pyenv --version
pyenv rehash
```

pyenv치면 정보가 뜬다.

```bash
pyenv install 3.7.2
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

requirement.txt에 있는 내용으로 환경설정을 할 수도 있다.

```bash
pip install -r requirement.txt
```



![dj_local1](image/dj_local1.JPG)



## mac

zzu.li/c9 내용대로 하고

로컬에서 할 때는 각각의 버전이 다를 수 있으므로 `.python-version` 폴더를 없애주어야 한다.

애초에 `gitignore`에 등록해주도록 하자.

```bash
rm -rf .python-version
```

가상환경 실행할 폴더로 이동해서 아래 명령어를 실행해준다.

```bash
pyenv local '가상환경 이름'
```

pip 환경을 확인하자.

```bash
pip list
```

requirement.txt에 있는 내용으로 환경설정을 할 수도 있다.

```bash
pip install -r requirement.txt
```



ㅔ