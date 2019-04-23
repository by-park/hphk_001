// 5.let-const.js
// var 함수단위 스코프
// let, const 블록단위 스코프

let name = 'name' // 변수
name = 'jason'
// console.log(name)

const gender = 'man' // 상수: 변하지 않음
// gender = 'woman'
// console.log(gender)

function test() {
    const color = 'red'
    if (true) {
        console.log(color) // 상위 스코프 거는 접근 가능
        let car = '소나타' 
    }
    console.log(car) // 하위 스코프 꺼는 접근이 안 된다.
}

test()