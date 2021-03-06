# Git

[TOC]

> 분산형 버전 관리 시스템, 코드의 history를 관리하는 도구

![git_flow](8. Picture\git_flow.PNG)



## git bash 설정

#### 1. 초기 설정

```powershell
$ git config --global user.name "아이디"
$ git config --global user.email "이메일"
```

아이디와 이메일을 등록해줘야 누가 작업하고 있는지 알 수 있다.

삭제 명령어랑 변경 명령어도 있는데 구글링 하면 나옴.



#### 2. 작업내용 원격 저장소로 보내기

```powershell
$ git init 
# 해당 폴더를 마스터 폴더로 지정해 저장소(repo)로 만듬. 한번 하면 더 할 필요 없음.
# 반드시 현재 디렉토리에 git을 사용하고 있는지, (master)가 있는지 확인 할 것.
```

```powershell
$ git status		
# 현재 상태 확인. 항상 쓰는 습관을 들이자
```

```powershell
$ git add . 		
# .은 리눅스에서 현재 디렉토리라는 뜻, 커밋할 목록을 업로드
# .대신에 특정 파일만 업로드 할 수 잇음
```

```powershell
$ git commit -m "비고 입력" 	
# 현재 상황을 스냅샷 처럼 저장.
```

```powershell
$ git log 
# 이력 나열
```

```powershell
# 사전에 github등에 저장소(repository)를 만들어 놓는다.
$ git remote add origin https://github.com/dmlimgo/TIL.git
# github 저장소를 origin으로 저장
$ git push -u origin master
# 원격저장소로 보낸다.
```



#### 3. 다른 컴퓨터에서 사용하기

```powershell
$ git clone 'github의 주소'
```

폴더에 접근한 후 명령어를 입력하면 git의 자료들이 복사됨.

`git init` 하지 말 것. 또 다른 repo가 생성된 것으로 간주되어 충돌 됨.

작업 종료 후 push하면 됨.



#### 4. 원격 저장소에서 가져오기

```powershell
$ git pull origin master
```



#### 5. 원격 저장소 복제하기

```powershell
$ git clone 주소복사
```



#### 6. 뺄것 빼고 푸시하기

```powershell
www.gitignore.io 접속
> 파이썬에서는 이런걸 빼는게 좋아라는 걸 알려줌
python을 치면
밑에 jupyter notebook 항목 확인
```

```powershell
폴더에 들어가서
.gitignore라는 파일을 확장자 없이 생성
폴더나 파일 입력하고 저장
```



#### 7. 변경사항 없애기

```powershell
$ git stash # working directory에 있는 변경사항을 임시공간으로 옮겨둠.
$ git stash pop # 변경사항이 다시 돌아옴?
```



#### 8. 커밋 수정하기

```bash
$ git commit --amend
```

수정 후 exit 엔터



#### 9. git log

```bash
$ git log
```

후 :를 이용해서 빠져나오기



#### 10. 엔터키 눌린?상태로 터미널 쓰고 싶을때?

```bash
$ vi ~/.bashrc
PS1을찾아서 마지막에\n을 추가하면 된다.
PS1 = ~~~(%s)") \n$ '
요렇게
```



vi ~/.bashrc





## Branch

#### git checkout -b '*branchname*'

> branch를 생성하고 이동

git branch '*branchname*' 과 git checkout '*branchname*' 을 합친것과 같다.

![git1](image/git1.JPG)



#### git checkout master

> master로 이동

![git2](image/git2.JPG)



#### git branch

> branch 확인

![git3](image/git3.JPG)



#### git merge *branchname*

> 브랜치와 master(현재상태)를 합친다



#### git branch -d *branchname*

> 브랜치 삭제

대문자 D는 진짜 어쩔 수 없을 때(코드가 아예 못 쓰게 되었을 때) 강제 삭제할 때 쓴다.



#### rebase

> 이런 용어는 거르자. 커밋 이력을 바꿔버림.



#### 일어날 수 있는 상황들

- 서로 다른 파일을 추가하고 수정했을 경우

  - Merge made by the 'recursive' strategy. 가 뜨면서 자동으로 잘 합쳐진다.

- 같은 파일을 수정했을 경우
  ```bash
  student@DESKTOP MINGW64 ~/Desktop/gitbranch (master)
  $ git merge jeong
  Auto-merging profile.txt
  CONFLICT (content): Merge conflict in profile.txt
  Automatic merge failed; fix conflicts and then commit the result.
  ```

  두개의 브랜치를 태깅을 해줌

  ```txt
  <<<<<<< HEAD
  프사 이미지 100*100
  반갑습니다^^
  =======
  프사 크기 300*300
  안녕.
  >>>>>>> jeong
  ```

  Visual Studio Code에서는 마우스 클릭만으로 어떻게 수정할지 정할 수 있다.

  수정을 마치고 난 이후에는 

  ```bash
  /gitbranch (master|MERGING)
  ```

  를 계속 띄워줌으로써 merge와 commit을 해야한다고 말해준다.

  `git add .`후 `git commit`해주면 된다.
