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
    // document.write(parsedData.content)
})