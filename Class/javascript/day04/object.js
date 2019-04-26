// 사람
/*
// 파이썬 버전
class Person():
    def __init__(self, name):
        self.name = name

donghoon = Person('donghoon')
*/

// 자바스크립트 버전
donghoon = {
    name:'donghoon',
    
    poop(){
        return "끙"
        // 혹은 console.log("끙")
    }
}

console.log(donghoon.name)
console.log(donghoon.poop())

junse = {
    name:'junse',
    
    poop: function(){
        return "poop"
    }
}

console.log(junse.name)
console.log(junse.poop())

/*
// 파이썬 버전
class Person:
    def __init__(self, name):
        self.name = name
    def poop(self):
        return "poop"
    def hello(self):
        return f"안녕 나는 {self.name}야"
*/

class Person {
    constructor(name){
        this.name = name
    }

    poop() {
        return "poop"
    }

    hello() {
        return `안녕 나는 ${this.name}야`
    }
}