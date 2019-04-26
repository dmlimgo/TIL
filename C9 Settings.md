# C9 Settings

> 19.01.28. 실습, c9에 실습 파일 있음.
>
> `zzu.li/c9`를 참조한 내용임.

Cloud9에서 웹 프로그래밍을 하기 위해서는 몇가지 환경을 설정해주어야 한다.

### 1. pyenv 설정

명령어를 입력하기 전에 명령어의 의미를 살펴보자.

- `pyenv` : 하나의 컴퓨터 내에서 여러가지 버전의 python을 사용할 수 있도록 버전관리를 도와준다.

- `pyenv global` : 전체 전역 파이썬 버전 설정

- `pyenv local `: 해당 디렉토리 파이썬 버전 설정

먼저 `c9.io/login` 페이지 접속 - `workspace` 생성 (`blank`로 생성해야 함)

아래 명령어를 통채로 복사해서 붙여넣으면 알아서 진행이 된다.

마지막에 엔터를 눌러 마지막 명령어를 실행시켜주는 것을 잊지 말자.

```powershell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.8
pyenv global 3.6.8
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
pyenv virtualenv 3.6.8 django-venv
pyenv local django-venv
pip install --upgrade pip
pip install django==2.1.8
echo '===========setting==========='
pip list
python -V
echo '===========setting==========='
```

* `echo 'export'` : pyenv path 설정
* `echo -e` : path 설정 불러오는거?

완료 후 아래 명령어 복사

```powershell
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

플라스크 할사람은 아래것도 복사

```powershell
pyenv virtualenv 3.6.7 flask-venv
pyenv local flask-venv
```

![0](8. Picture\0.PNG)

가상환경을 만들었다.

flask 설치를 위한 명령어 입력

```powershell
pip install flask 
```

![0](8. Picture\0-1.PNG)

pip 업그레이드를 위한 명령어 입력

```powershell
pip install --upgrade pip
```

![0](8. Picture\0-2.PNG)

```powershell
pip freeze > req.txt 
```

입력 하면 txt파일 생김. (pip의 버전 리스트를 생성 > 이걸 토대로 다른 사람들이 가상환경 설치를 할 수 있음.)

flask 홈페이지의 내용을 기반으로 진행.

python 파일 생성 후

flask run -h $IP -p $PORT 으로 페이지 링크가 나옴.

```python
if __name__ == '__main__':
# host와 port 설저은 c9에서 실행시키기 위해서 설정한 것이다.
# 아래와 같이 설정하면 python app.py로 실행 가능함.
	app.run(host='0.0.0.0', port='8080', debug=True)
```

### 2. Git

> c9은 기본적으로 workspace에서 git config가 가입한 이메일로 되어있기 때문에 github에 커밋 기록을 제대로 남기기 위해서 설정해준다.

```powershell
git config --global user.name ______
git config --global user.email ______
```



### 9. 기타설정

- timezone 설정

```bash
sudo dpkg-reconfigure tzdata
```

