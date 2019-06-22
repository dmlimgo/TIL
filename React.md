# React

> DOM 관리와 상태값 업데이트 관리를 최소화하고, 오직 기능 개발과 사용자 인터페이스를 구현하는 것에 집중 할 수 있도록 하기위해서 만들어진 프레임워크.
>
> "컴포넌트" 라는 개념에 집중이 되어있다. 공식 라이브러리가 있는 것이 아니어서 개발자가 원하는 스택을 골라 쓸 수 있다.
>
> Virtual DOM을 이용해 가상 DOM에 렌더링을 하고 기존의 DOM과 비교를 해서 업데이트가 필요한 곳에만 업데이트를 해줘 DOM 변화를 최소화 해준다.



## 준비하기

1. Node.js : Webpack이나 Babel같은 도구들이 Node.js를 기반으로 만들어져 있기 때문에 설치해야 한다.

2. Yarn : 조금 개선된 버전의 npm이라고 생각하면 된다. 더 나은 속도, 더 나은 캐싱 시스템을 사용하기 위함.

   ```bash
   $ brew install yarn
   or
   $ npm install -g yarn
   ```

   버전 확인

   ```bash
   $ yarn --version
   ```

   설치 후 전역 사용에 문제가 있다면 Path 설정을 해준다.

   ```bash
   $ export PATH="$PATH:/opt/yarn-[version]/bin"
   ```

3. Create-react-app : React앱을 만들어주는 도구

   ```bash
   $ npm install -g create-react-app
   or
   $ yarn global add create-react-app
   ```

   yarn의 global설치의 경우 제대로 작동하기 위해선 윈도우라면 상관없지만, 리눅스 혹은 macOS라면 다음 커맨드도 입력해준다.

   ```bash
   # macOS
   echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.bash_profile
   # Linux
   echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.bashrc
   ```



## 시작하기

아래의 명령어를 입력해 앱을 생성하고 실행한다.

```bash
$ create-react-app [앱이름]
$ cd [앱이름]
$ yarn start
```



```bash

```

