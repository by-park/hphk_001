# Javascript 4강

2019-04-25 

콜백함수를 왜 써야하는가!

_1.callback.js_

```javascript
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

console.log(sum) // 15
```

_2.callback.js_ 콜백 지옥의 시작

```javascript
const orderCoffee = (order, callback) => {
    let coffee
    // 1초가 걸림!!
    setTimeout(()=>{
        coffee = order // 다 만듬
        callback(coffee)
    }, 1000); 
    return coffee
}

orderCoffee('Americano', console.log)
```

_3.promise.js_ 콜백지옥에서 벗어나는 Promise 문법

```javascript
const orderCoffee = (order) => {
    return new Promise((resolve, reject)=>{
    let coffee 

    setTimeout(()=>{
        if (order === undefined){
            reject('손님 주문 안 하셨는데요;')
        }
        // 다 만들면 coffee를 넘겨줄게
        coffee = order
        resolve(coffee)
    }, 1000);
})}

orderCoffee('Americano')
    .then((coffee)=>{ // 그리고
        console.log(`${coffee} 잘 마실게요!`)
    }) // Promise 객체 반환
    .catch((error)=>{
        console.log(error)
    })
```

