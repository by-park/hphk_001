# Javascript 5강 - OOP

2019-04-26

파이썬에서 객체를 생성하는 방법

```python
// 파이썬 버전
class Person():
    def __init__(self, name):
        self.name = name

donghoon = Person('donghoon')
```

자바스크립트에서 object를 생성하는 방법 (돌릴 때는 node 사용해서 돌리기)

```javascript
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
```



ES6 이후 class 선언이 가능해졌다.

파이썬 class 버전

```python
// 파이썬 버전
class Person:
    def __init__(self, name):
        self.name = name
    def poop(self):
        return "poop"
    def hello(self):
        return f"안녕 나는 {self.name}야"

donghoon = Person("동훈")
```

자바스크립트 class 버전

```javascript
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

const donghoon = new Person("동훈")
```

