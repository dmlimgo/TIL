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

### 1. App.js

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



### 2. index.js

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



### 3. JSX (javascript XML)

- 태그는 꼭 닫혀있어야 함 input이나 br도 닫아줘야 한다.
- 두개 이상의 엘리먼트는 무조건 하나의 엘리먼트로 감싸져있어야 한다.
- JSX내부에서 자바스크립트 값을 사용할 땐 {변수명}과 같이 이용할 수 있다.

- 조건부 렌더링은 삼항 연산자나 AND 연산자를 사용한다. if문은 IIFE(즉시 실행 함수 표현)을 사용한다.

  ```js
  <div>
    {
      1 + 1 === 2
      ? (<div>맞아요!</div>)
    	: (<div>틀려요!</div>)
    }
  </div>
  ```

  ```js
  <div>
    {
    	(function() {
        pass
      })()
  	}
  </div>
  or arrow function
  ```

- 주석은 `{/*...*/}` 사이에 넣거나 태그 사이에 넣을 수도 있다.



### 4. Style과 className

- style은 다음과 같이 적용할 수 있다.

  ```js
  const style={backgroundColor: 'black'};
  ...
  <div style={style}>
    hi
  </div>
  ```

- class은 App.css에 class를 선언하고 className으로 사용할 수 있다.



### 5. 새 컴포넌트 만들기

- 받아온 값은 `this.props`로 표시 가능하다.
- 기본값은 `defaultProps`에 설정한다.

#### 5.1 함수형 컴포넌트

- 단순히 props만 받아서 보여주는 컴포넌트의 경우 함수형 컴포넌트로 간편하게 작성할 수 있다.

### 

### 6. State (동적 데이터)

- Class fields 문법 사용, 사용하지 않는다면 constructor 사용(불편하고 느림)
- arrow function을 사용하지 않으면 this사용이 불편(constructor를 쓰지 않으면 undefined로 나타남.)

#### 6.1 setState

- React에서는 이 함수가 호출되면 컴포넌트가 리렌더링 되도록 설계되어 있다.

- 객체의 깊숙한곳 까지는 확인하지 못한다.

  ```js
  state = {
    number: 0,
    foo: {
      bar: 0,
      foobar: 1
    }
  }
  ```

  에서 아래와 같이 한다고 foobar의 값이 업데이트 되지 않는다.

  ```js
  this.setState({
    foo: {
      foobar: 2
    }
  })
  ```

  대신 기존의 foo객체가 바뀌어버린다.

  따라서 다음과 같이 해 주어야 한다.

  ```js
  this.setState({
    number: 0,
    foo: {
      ...this.state.foo,
      foobar: 2
    }
  })
  ```

  …은 자바스크립트의 전개연산자이다. 

  귀찮은 방법이므로, immutable.js 나 immer.js를 사용할 것이다.

- 객체 대신 함수 전달하기 

  - 비구조화 할당(destructuring assignment) : 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 자바스크립트 표현식. 

  	```js
  this.setState({
    number: this.state.number + 1
  })
  	```
	
  	을 함수를 전달하는 방식으로 아래와 같이 작성할 수 있다.
	
  	```js
  	this.setState(
  		(state) => ({
  	    number: state.number
  	  })
  	)
  	```
  	
  	비구조화 할당을 사용하면 다음과 같이 작성할 수 있다.
  	
  	```js
  	this.setState(
  		({number}) => ({
  	    number: number + 1
  	  })
  	)
  	```
  	
  	잘 이용하면 아래와 같이도 사용할 수 있다.
  	
  	```js
  	const { number } = this.state;
  	this.setState({
  	  number: number + 1
  	})
  	```
  
  

### 7. 이벤트 설정

React에서는 다음과 같이 이벤트를 설정한다.

```js
<button onClick={this.handleDecrease}>-</button>
```

반드시 **주의**해야 할 것은

- 이벤트 이름은 lowerCamelCase로 해주어야 한다.
- 이벤트에 전달해주는 값은 메소드`this.handleIncrease()`가 아니라 함수`this.handleIncrease`이어야 한다. 



### 8. LifeCycle API

> 컴포넌트가 브라우저에서 나타날 때, 사라질 때, 업데이트 될 때 호출되는 API이다.

1. render()
2. getSnapshotBeforeUpdate()
3. 실제 DOM에 변화 발생
4. componentDidUpdate

#### 8.1 컴포넌트 초기 생성

- constructor
- componentWillMount (deprecated) => UNSAFE_componentWillMount
- componentDidMount 

#### 8.2 컴포넌트 업데이트

- ComponentWillReceiveProps (deprecated) => UNSAFE_componentWillReceiveProps or getDerivedStateFromProps

- [NEW] static getDerivedStateFromProps

- shouldComponentUpdate

- componentWillUpdate (deprecated) => [NEW] getSnapshotBeforeUpdate 

  : DOM 변화가 일어나기 직전의 DOM 상태를 가져오고, 여기서 리턴하는 값은 componentDidUpdate에서 3번째 파라미터로 받아올 수 있다.

- componentDidUpdate(prevProps, prevState, snapshot)

  : 컴포넌트에서 render()를 호출하로 난 다음에 발생. 실제로 업데이트 해준다.

#### 8.4 컴포넌트 제거

- componentWillUnmount

  : 주로 등록했었던 이벤트를 제거하고, setTimeout이나 외부라이브러리를 제거한다.

#### 8.5 컴포넌트에 에러 발생

- componentDidCatch



### 9. input 상태 관리

- input > onChange : input의 텍스트 값이 바뀔 때마다 발생하는 이벤트.

- `Computed property names` 

  ```js
  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    })
  }
  ```

#### 9.2 부모 컴포넌트에게 정보 전달하기