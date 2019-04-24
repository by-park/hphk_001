// POST를 통한 posts 생성
const URL = "https://jsonplaceholder.typicode.com/posts"

const XHR = new XMLHttpRequest()

// 1. XHR.open()
XHR.open('POST', URL)

// 2. XHR.setReuestHeader (헤더정보)
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
)

const data = {
    userId: 1,
    title: "옛다 제목이다",
    body: "내용 받아라"
}
XHR.send(JSON.stringify(data))

// 3. XHR.addEventListener()
XHR.addEventListener('load', function (donghoon){
    console.log(donghoon.target.status) // 성공했다는 201코드
    console.log(donghoon.target.response)
})