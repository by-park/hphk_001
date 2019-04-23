Javascript 1강&2강

2019-04-22 ~ 2019-04-23

- 자바스크립트는 **브라우저를 조작**하기 위한 언어이다!

- 파이썬과 비교해보면 개념으로 바뀌어있다!

> 변수: 변수
>
> 리스트: 배열
>
> 딕셔너리: 오브젝트

- 자바스크립트 작성

HTML 문서 내에서 `<script></script>` 안에 작성해도 되고, `<script src="파일이름.js">`로 불러와서 사용해도 된다.

- 조건문

```javascript
user_name = prompt("이름이 뭐야?")
user_name = prompt("나이를 입력해줘")

if (user_age > 30) {
    age = '아재네'
} else if (user_age > 20) {
    age = '아재 아니네'
} else {
    age = '학생이네'
}
document.write("<h1>너!</h1>")
document.querySelector('h1').innerText = `${user_name}은(는) ${age}`
// 혹은 alert('') 로 메세지 팝업 띄울 수 있다.
```

- 반복문

```javascript
user_input = prompt("숫자를 입력해줘")
for (i = 0; i < user_input' i+=1') {
    document.write('<p>안녕</p>')
}
```

- 함수

```javascript
function getMin(a, b){
    if (a > b) {
        return b
    }
    return a // return을 만나면 나가기 때문에 else 문이 필요하지 않다.
}

var min = getMin(3, 4)
console.log(min)
```

```javascript
function getMinFromArray(numbers){
    var min = Infinity
    // TODO: 배열에서 최소값을 구하여 min에 할당
    for (num of numbers){
        if (min > num){
            min = num
        }
    }
    return min
}

var numbers = [1, 2, 3, 4, 5]
var min = getMinFromArray(numbers)
console.log(min)
```

- node js 설치

node js 설치 페이지로 가서 download 탭 > window > 64 를 설치한다. 새로운 폴더를 만들고 git bash에서 code . 을 눌러서 vs code를 실행시킨다. npm init을 치면 바로 노드 환경이 만들어진다!

- lodash 모듈 사용

랜덤 등이 자바스크립트에서는 지원이 되지 않기 때문에, 이런 것들을 가능하게 해줄 lodash를 설치한다. 터미널에 `npm install lodash`를 통해 설치한다.

```javascript
var _ = require('lodash')
var menus = ['짜장면', '짬뽕', '볶음밥'] // Array (배열) 라고 부른다.
var pick = _.sample(menus)
console.log(`오늘의 메뉴는 ${pick}`) // string 안에 변수를 넣고 싶을 때
```

```javascript
const luckyNumbers = [5, 7, 32, 2, 36, 26]

function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    let count = 0
    for (pick of picks) {
        if (_.includes(luckyNumbers, pick)) { // luckyNumbers.includes(pick)
            count = count + 1;
        }
    }
    console.log(count)
}

match()
```

