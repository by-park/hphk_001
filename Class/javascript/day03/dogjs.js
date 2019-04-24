// 30 분 뒤에 종료를 알리는 js 코드
function sleep(){
    let start = Date.now()
    while (Date.now() < start + 5000){}
}

function finish(){
    // setTimeout(function(){
    //     console.log('수업이 종료되었습니다.')
    // }, 1000)
    sleep()
    console.log("수업이 종료되었습니다.")
}

console.log("수업 중")
finish()
console.log("땡땡땡")