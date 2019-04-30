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


/*
const coffee = orderCoffee('Americano')
console.log(coffee)
*/ //원하는 형태

const getCoffee = async () => {
    const coffee = await orderCoffee('Americano')
    console.log(coffee) // Americano
}

getCoffee()

const getData = async () => {
    try{
        const URL = 'https://koreanjson.com/posts/1'
        const response = await fetch(URL) // 데이터를 불러오겠다.
        const data = await response.json() // 파싱하겠다.
        console.log(data)
    } catch (error) {
        console.log(error)
    }
}