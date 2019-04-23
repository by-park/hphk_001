const dooly = document.querySelector('#dooly')

console.log(dooly)

// 둘리를 클릭하면, 호이라고 한다.

dooly.addEventListener('click', function() {
    alert('호이')
})

let x = 0;
let y = 0;

document.addEventListener('keydown', function(event) {
    // console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        y += 30
        dooly.style.marginBottom = `${y}px`;
    } else if (event.keyCode === 40) {
        y -= 30
        dooly.style.marginBottom = `${y}px`
    } else if (event.keyCode == 37) {
        x -= 30
        dooly.style.marginLeft = `${x}px`
    } else if (event.keyCode == 39) {
        x += 30
        dooly.style.marginLeft = `${x}px`
    }
})

