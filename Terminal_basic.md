# Terminal basic

[TOC]

---





## Git bash

[Git bash 공식 사이트](https://gitforwindows.org)

터미널 중 하나로 CLI (Command Line Interface)를 사용.

* `Shell`은 운영체게제서 사용자가 입력하는 명령을 읽고 해석하여 대신 실행해주는 프로그램. 사용자와 운영체제의 커널(내부) 사이의 인터페이스를 감싸는 층이기 때문에 붙은 이름.
* `bash`는 커맨드 쉘의 일종으로 새로 태어났다는 뜻의 `Born Again`과 초기의 유닉스 쉘인 `본 쉘(Bourne Shell)`이 합쳐져 `Bourne-again Shell`이라고 불리다가 `bash`라고 줄여 부르게 됨.
* `.bashrc(bash run commands)` 터미널을 열 때마다 실행 됨.
* `.bash_profile` 개별 사용자에 대한 설정들이 있음.

#### 1. 기본 명령어

`$ ls (list)` : 현재 폴더의 파일 리스트

```powershell
$ cd 폴더명
# 상대경로 접근 (change directory)
$ cd ~/Desktop/python/등등
# 절대경로 접근
$ cd .. 
# 상위 폴더로
```

`$ touch` : 파일 만들기
`$ mk dir` : 폴더 만들기
`$ rm` : 파일 지우기
`$ rm -rf(reculsive force)` : 폴더 지우기
`$ mv` : 파일명 바꾸기
`$ pwd (present working director)` : 현재 작업중인 폴더 확인



#### 2. 터미널에서 python 실행하기

파이썬을 설치한 상태여야 함

```powershell
$ cd ~
```

를 입력해서 home folder로 접근한다.

```powershell
$ touch .bashrc
```

bashrc 파일을 생성한다.

```powershell
$ vi ~/.bashrc
```

bashrc 파일에 접근해서

i를 눌러 수정가능하게 한 뒤에 아래의 내용을 입력한다.

```powershell
alias python='winpty python.exe'
```

`alias`는 별명이라는 뜻

`winpty` Windows software package providing an interface similar to a Unix pty-master for communication with Windows console programs.

이후 python을 입력해 실행가능.