## jupyter notebook

### 1. 기본 설정

#### 1) 설치하기

```powershell
$ pip install jupyter notebook
```

* 설치 끝나면 업데이트 자동으로 하는거 명령어 뜸 그것도 입력

```powershell
$ jupyter notebook
```

* 명령어로 실행

* `ctrl + c` 로 종료

#### 2) 추가 확장

##### (1) nbextensions

> 각종 설정을 할 수 있게 해준다.

```powershell
$ pip install jupyter_contrib_nbextensions
$ jupyter contrib nbextension install --user
```

하면 `jupyter notebook`에 `nbextensions` 탭이 추가됨.

#### 3) 폰트 설정

* D2 font 사용

사용자 > 사용자폴더 > .jupyter > custom폴더 생성 > custom.css파일 생성

```python
.CodeMirror {font-family: D2Coding;}
```

입력 후 저장

서버 재부팅