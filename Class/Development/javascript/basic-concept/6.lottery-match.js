// 6.lottery-match.js
const luckyNumbers = [5, 7, 32, 2, 36, 26]
const _ = require('lodash')

/*
const numbers = _.range(1, 46) // 1~45
const picks = _.sampleSize(numbers, 6) // Camel case 낙타처럼 중간에 등을 뽈록 올라와서 이렇게 부른다.
console.log(`오늘의 행운의 번호는 ${picks}`)

function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    // const inter = _.intersection(luckynumber)
    lucky = _.size(_.intersection(luckynumbers, picks))
    // return lucky
    console.log(lucky)
}

match()

*/

// console.log(match())

// function match(numbers) {
//     let sum = 0;
//     for (num of numbers) {
//         for (lucknum of luckyNumber) {
//             if (num==lucknum) {
//                 sum = sum+1;
//             }
//         }
//     }
//     return sum
// }

// console.log(match(picks))


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
// console.log(match(), 6)