// 이건 한줄 주석
/*
    이건 여러줄 주석
*/
// alert("야!")
user_name = prompt("이름이 뭐야?")
user_age = prompt("나이를 입력해줘")
console.log(user_age)

if (user_age > 30) {
    age = '아재네'
    // alert('아재네')
} else if (user_age > 20) {
    age = '학식이네' 
    //alert('학식이네')
} else {
    age = '급식이네'
    //alert('급식이네')
}

document.write("<h1>너!</h1>")
//document.querySelector('h1').innerText = user_name + "는" + age
document.querySelector('h1').innerText = `${user_name}은(는) ${age}`

// console.log("임마!")
// console.log(document.querySelector('h1'))
// console.log(document.querySelector('h1').innerText)

user_input = prompt("숫자를 입력해줘")
for (i = 0; i < user_input; i+=1) {
    document.write('<p>안녕</p>')
}
