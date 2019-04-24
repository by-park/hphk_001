# Javascript 3강

2019-04-24

- ajax 콜

```javascript
// AJAX (Asynchronous Javascript and XML)
// XHR(XMLHttpRequest) => 모든 브라우저에 built in 되어있는 객체
// fetch => ES6 이후로 나온 ajax 함수

const XHR = new XMLHttpRequest() // class
const URL = 'https://www.koreanjson.com/posts/1'

XHR.open('GET', URL)
XHR.send()

XHR.addEventListener('load', (event) => {
    const rawData = event.target.response
    const parsedData = JSON.parse(rawData) // String => Object
    // JSON.stringify() // Object => String
    console.log(parsedData)
    // document.write(parsedData.content) // 이걸 쓰면 페이지에 바로 써진다.
})
```

이것을 실습해볼 때는 node 환경에서 돌아가지 않기 때문에 브라우저 콘솔 창을 열어서 위의 내용을 복사 붙여넣기 해줘야한다.

- Giphy Search Engine 만들기

https://developers.giphy.com/ 에 가입하고 APP을 생성해서 API 키를 발급받는다.

_index.html_

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Giphy Search Engine</title>
    <link rel="stylesheet" href="./main.css">
</head>
<body>
    <div class="container container-padding50">
        <input id="js-userinput" type="text" class="container-textinput">
        <button id="js-go" class="container-button">Go!</button>
    </div>
    <div id="result-area" class="container container-padding50 js-container">
    </div>
    <script src="./main.js"></script>
</body>
</html>
```

_main.css_ 

```css
body {
    width: 80%;
    max-width: 1024px;
    margin: 0 auto;
    background-color: black;
}

h1 {
    color: white;
}

.img-center {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.container-padding50 {
    padding-top: 50px;
}

.container-textinput {
    width: 80%;
    display: inline-block;
    padding: 20px;
    font-size: 16px;
    font-family: Helvetica, sans-serif;
}

.container-button {
    width: 10%;
    display: inline-block;
    padding: 20px;
    background-color: green;
    color: white;
    font-size: 16px;
    font-family: Helvetica, sans-serif;
    border: 1px solid green;
    border-radius: 5px;
}

.container-image {
    width: 30%;
    display: block;
    float: left;
    margin-right: 3%;
    margin-bottom: 5%
}
```

_main.js_

```javascript
// 1. input 태그 안의 값을 잡는다.
const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {
    const value = input.value
    searchAndPush(value)
})

input.addEventListener('keypress', (e) => {
    // console.log(e)
    if (e.keyCode == 13) {
        const value = input.value
        searchAndPush(value)
    }
})
// 2. Giphy API 를 통해 data를 받아서 가공한다.
// https://developers.giphy.com/
const searchAndPush = (keyword) => {
    resultArea.innerHTML = null
    const API_KEY = '발급받은 키를 여기에 입력하기'
    const URL = `https://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    const GiphyXHR = new XMLHttpRequest()
    GiphyXHR.open('GET', URL)
    GiphyXHR.send()

    GiphyXHR.addEventListener('load', (e) => {
        const rawData = e.target.response
        // console.log(rawData) // 엄청나게 많은 데이터가 넘어온다!
        const parsedData = JSON.parse(rawData)
        for (data of parsedData.data) {
            pushToDom(data.images.fixed_height.url)
        }
        // pushToDom(parsedData.data[0].images.fixed_height.url)
        
    })

    // 3. gif 파일들을 index.html(DOM) 에 밀어 넣어서 보여준다.
    const pushToDom = (data) => {
        const img = document.createElement('img') // <img></img>
        img.setAttribute('src', data) // <img src="${data}"/>
        img.className = 'container-image' // === setAttribute('class', 'container-image') 와 같은 작업
        resultArea.appendChild(img)
        // resultArea.innerHTML += `<img src="${data}"/>`
}
}
```

- javascript는 non-blocking 함수들이 있다! setTimeout() 함수 같은 건 만나면 어 형님, 지나가겠습니다! 하고 다른 함수들 먼저 실행하고, 이 함수는 시작은 했지만 이벤트 리스트에 넣고 계속 확인한다.