// 3. promise.js
// 다 만들면 커피를 줄게라는 약속을 할 거임
// 중간에 무슨 일이 생기면 알려줄 거임

const sum = (a, b) => {
    return a + b
}

// const sum (a, b) => a + b // 이렇게 바로 리턴한다고 짧게 쓸 수 있다.

// resolve 에 성공시 넘겨줄 객체
// reject 에 무슨 일이 생길시 발생시킬 에러를 담음
const orderCoffee = (order) => new Promise((resolve, reject)=>{
    let coffee 

    setTimeout(()=>{
        if (order === undefined){
            reject('손님 주문 안 하셨는데요;')
        }
        // 다 만들면 coffee를 넘겨줄게
        coffee = order
        resolve(coffee)
    }, 1000);
})


// 리턴한다는 것이 잘 보이도록 다음과 같이 수정하였다.
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

orderCoffee('Americano')
    .then(coffee=>{ console.log(`${coffee} 잘 마실게요!`)}) // Promise 객체 반환
    .then(test=>{ console.log(test)}) // undefined

orderCoffee('Americano') // Promise 에 Americano가 담긴다.
    .then(coffee => {
        console.log(coffee) // Americano
        return orderCoffee('Latte') // 새로운 Promise가 생성됨
    })
    .then(coffee => {
        console.log(coffee)
        return // undefined가 나옴
    })
    .then((coffee)=>{
        console.log(coffee) // undefined
    })

    
/*
const orderCoffee = (order) => {
    let coffee 

    setTimeout(()=>{
        // 다 만들면 coffee를 넘겨줄게
        coffee = order
    }, 1000);
}
*/