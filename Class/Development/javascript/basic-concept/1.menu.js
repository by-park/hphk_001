var _ = require('lodash')
var menus = ['짜장면', '짬뽕', '볶음밥'] // Array (배열) 라고 부른다.

var pick = _.sample(menus)
// console.log(pick)

console.log(`오늘의 메뉴는 ${pick}`) // string 안에 변수를 넣고 싶을 때