# JS_event listener

> 이벤트가 발생했을 때 그 처리를 담당하는 함수



## 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .bg {
            background-color: #F7F7F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
    </style>
</head>
<body>
    <div class="bg">
        <img id="dino" width="100px" heigth="100px" src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg" alt="dino">
    </div>

    <script>
    </script>
</body>
</html>
```

```js
// 1)무엇을
const dinoImage = document.querySelector('#dino')
// 2)언제
dinoImage.addEventListener('click', function(e) {
    // object의 객체를 받아 볼 수 있음.
    console.log(e)
    // 3)무엇을 하겠다. (EventListener에서는 Arrow Function을 쓸 수 없다.)
    const bgDiv = document.querySelector('.bg')
    bgDiv.append('크앙')
})
```





## EventListener

> 주의할 점, EventListener에서의 콜백함수에서는 `arrow function`을 사용하지 않는다.

#### *object*.addEventListener(*value*, *func*)

```js
// 무엇을
const dinoImage = document.querySelector('#dino')
// 언제
dinoImage.addEventListener('click', function(e) {
    // object의 객체를 받아 볼 수 있음.
    console.log(e)
    // 무엇을 하겠다. (EventListener에서는 Arrow Function을 쓸 수 없다.)
    const bgDiv = document.querySelector('.bg')
    bgDiv.append('크앙')
})
```

##### *value* = 'click'

> 마우스 버튼을 클릭하고 버튼에서 손가락을 떼면 발생한다.

```js
위 예제를 보자
```

##### *value* = 'keydown'

> keyCode 값에 따라 동작하고자 할 때 쓴다.

```js
let x = 0
let y = 0
const dinoImage = document.querySelector('#dino')
document.addEventListener('keydown', function(e) {
    console.log(e)
    if (e.keyCode === 37){
        console.log('왼쪽으로가')
        x -= 30
        dinoImage.style.marginLeft = `${x}px`
    }
    else if (e.keyCode === 38){
        console.log('위로가')
        y += 30
        dinoImage.style.marginBottom = `${y}px`
    }
    else if (e.keyCode === 39){
        console.log('오른쪽으로가')
        x += 30
        dinoImage.style.marginLeft = `${x}px`
    }
    else if (e.keyCode === 40){
        console.log('아래로가')
        y -= 30
        dinoImage.style.marginBottom = `${y}px`
    }
})
```

##### *value* = 'copy'

> Ctrl+C 등의 복사 단축키에 대한 동작을 한다.

```js
document.addEventListener('copy', function(e){
    console.log(e)
    e.preventDefault()
    alert('복사 금지')
})
```


