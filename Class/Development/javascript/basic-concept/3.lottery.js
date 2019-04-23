// 3.lottery.js
var _ = require('lodash')
var numbers = _.range(1, 46) // 1~45
var picks = _.sampleSize(numbers, 6) // Camel case 낙타처럼 중간에 등을 뽈록 올라와서 이렇게 부른다.
// console.log(`오늘의 행운의 번호는 ${picks}`)
//console.log(numbers) // 터미널에 node 3.lottery.js 하면 1~45까지 출력되었다.

var name = 'jason'
var baseURL = 'www.naver.com'
console.log(`제 이름은 ${name}입니다. `) //그리고 나이는 ${age} 입니다.
console.log('제 이름은' + name)