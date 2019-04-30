// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'


// axios.get(URL) // AJAX CALL 비 동기적으로 동작하는 함수이다. 이게 뭘 반환? // => 비동기 함수는 대개 프로미스를 반환한다.
//     .then(response => {
//         const imageUrl = response.data.message
//         const imageBox = document.querySelector('#img-div')
        
//         const image = document.createElement('img')
//         image.src = imageUrl
//         imageBox.appendChild(image)
//     })

// TODO: 위 코드를 async-await로 바꿔 써주세요.
const getImage = async () => {
    const response = await axios.get(URL) // 여기서 콘솔로 찍어보면 프로미스가 나온다. 이건 비동기 함수구나!
    const imageUrl = response.data.message
    const imageBox = document.querySelector('#img-div')
        
    const image = document.createElement('img')
    image.src = imageUrl
    imageBox.appendChild(image)
}

getImage()
getImage()
getImage()
getImage()