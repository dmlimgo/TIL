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

### App.js

컴포넌트를 만들기 위해서는 App.js파일을 보면 된다. 아래는 기본으로 주어지는 구조이다.

```js
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  
  return (
    <div className="App">
      리액트
    </div>
  );
}

export default App;
```

react를 불러오고 logo와 css를 불러오는 코드이다.

```js
import React from 'react';
import logo from './logo.svg';
import './App.css';
```

클래스를 이용해서 만드는 방법도 있는데 일단은 함수로 주어져 있으므로 함수로 진행한다.

함수 내부에는 JSX를 return해주는 코드가 있어야 한다.

```js
function App() {
  return (
    <div className="App">
      리액트
    </div>
  );
}
```

마지막으로 우리가 작성한 컴포넌트를 다른 곳에서 불러와서 사용할 수 있도록 내보내기를 해준다.

```js
export default App;
```



### index.js

기본으로 주어지는 코드는 다음과 같다.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
serviceWorker.unregister();
```

우리가 만든 컴포넌트를 다음과 같이 불러온다.

```js
import App from './App';
```

브라우저 상에 우리의 리액트 컴포넌트를 보여주기 위해서 `ReactDOM.render` 함수를 사용한다. 첫번째 파라미터는 렌더링 할 결과물이고, 두번째는 어떤 DOM에 그릴지 정해준다. 

```js
ReactDOM.render(<App />, document.getElementById('root'));
```

위 코드의 경우는 해당 파일 안에 있는

```js
<div id="root"></div>
```

를 찾아서 렌더링 해준다.

**태그는 꼭 닫혀있어야 한다. input이나 br태그도 닫아주어야 한다.**

