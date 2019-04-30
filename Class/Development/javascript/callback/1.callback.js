// 1.callback.js
// 1급 객체란
// 1. 인자로 넘길 수 있어야 한다.
// 2. 변수나 데이터에 할당할 수 있어야 한다.
// 3. 객체의 리턴값으로 리턴할 수 있어야 한다.
// String, number, boolean
// function



// 숫자로 된 배열을 받아서 모두 더한다.
const numberAddEach = (numbers) => {
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 뺀다.
const numbersSubEach = (numbers) => {
    let sum = 0
    for (const number of numbers) {
        sum -= number        
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 곱한다.
const numbersMulEach = (numbers) => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
    return sum
}

// numbersMulEach(numbers) // 이렇게 하면 곱하기를 해준다.
const numbers = [4, 5, 6]

const numbersEach = (numbers, callback) => {
    for (const number of numbers) {
        callback(number)
    }
}

let sum = 0

numbersEach(numbers, (number)=>{
    sum += number
    // console.log(`numbersEach `, number) // 4, 5, 6 출력이 되면 정상적인 것
})

let sum = 0
// ES6 이후로 도입된 Array Helper Method
numbers.forEach((number) => {
    sum += number
})

console.log(sum) // 15

/*

// 1. 인자로 넘길 수 있어야한다.
addEventListener('load', (event)=>{})

// 2. 변수나 데이터에 할당할 수 있어야 한다.
const sum = (a,b) => {
    return a + b
}

// 3. 객체의 리턴값으로 리턴할 수 있어야한다.
const log = () => {
    return 123
}

const test = log() // 123

// 위에 숫자를 주고 받듯이, 다음과 같이 함수를 리턴할 수 있다.
const log = () => {
    return sum
}

const sumCopy = log() // sum
sumCopy(1, 2) // 3
*/