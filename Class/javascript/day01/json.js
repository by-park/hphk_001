// JSON & javascript object

/*
1. JSON: 파일 포맷 & 단순 문자열(string)
"{
    coffee: 'Americano'.
    iceCream: 'Red Velvet'
}"
자바 스크립트 오브젝트와 비슷하게 생겼지만 실제로는 그냥 글자의 나열일 뿐이다.
이 문자열을 자바 스크립트가 읽을 수 있고 조작할 수 있게 만드는 작업이
제이슨을 자바 스크립트 오브젝트로 변환하는 과정이다.

2. Javascript Object: Javascript 코드가 읽을 수 있는 오브젝트
*/

// const stringObject = JSON.stringify('{"coffee":"Americano", "iceCream":"Red Velvet"}') 이걸로 확인해보셨다. 안에가 큰 따옴표, 바깥이 작은 따옴표여야한다.

JSONData = '{ "coffee":"Americano", "iceCream": "Red Velvet" }'

const parsedData = JSON.parse(JSONData)

console.log(parsedData.coffee)
console.log(typeof(JSONData))
console.log(typeof(parsedData))