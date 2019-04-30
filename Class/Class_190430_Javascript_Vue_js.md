# javascript 06강 (Vue.js)

2019-04-30

### Vue.js

- 뷰는 다른 것들에 비해 압도적으로 쉽다. + 가볍다 => 둘의 장점을 합쳤다. 
- React는 자유도가 높다. 잘 이해하고 있으면 거의 모든 걸 내가 만들어 쓸 수 있다.
- Angular는 자유가 가장 낮다. 처음에 규칙 외우면, 그거에 맞춰서만 돌아가서 편리하다. + 무겁다

### Vue.js 사용 코드 예시

- 뭔가 다운받을 필요 없이 CDN으로 가져오면 바로 사용할 수 있다!

_index.html_

```html
<body>
    <div id="app">
        <span v-html="header"></span>
        <h2>{{ subheader }}</h2>
        <ul>
            <li v-for="t in todo">{{ t }}</li>
        </ul>
        <p v-if="checked">{{ todo }}</p>
        <p>{{ donghoon }}</p>
        <ol>
            <li v-for="dh in donghoon">{{ dh }}</li>
        </ol>

        <input v-model="subheader">
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({
            el: '#app',
            data: {
                header: '<h1>Todo App</h1>',
                subheader: 'This is todo app',
                todo: ['동사무소 가기','입대확인증 뽑기','재입대하기'],
                donghoon: {
                    name: "동훈",
                    gunPil: true,
                    major: "기계공학"
                },
                checked: true,
                posts: [
                    {
                        id:1,
                        title: '제목1',
                        content: '내용2',
                    }, {}, {}, {}
                ],
                // 나중에는 위에가 아니라,
                posts: fetch('/posts') // /posts를 하면 바로 json이 들어오게 하는 형태가 될 것이다.
            }
        })
        // 장고버전으로 생각하면 무언가를 상속받아 쓰는 객체라고 생각하면 된다.
        // class Post(models.Model)
    </script>
</body>
```



### Axios

- XHR, fectch 대신에 Axios 라이브러리가 있다. 아직 정식 배포 전이지만 안정성이 높아서 많이 사용한다. 
- 비동기 함수이기 때문에 .then을 사용하거나 async, await를 사용할 수 있다.

_useAxios.js_

```javascript
// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'

axios.get(URL) // AJAX CALL 비 동기적으로 동작하는 함수이다. 이게 뭘 반환? // => 비동기 함수는 대개 프로미스를 반환한다.
    .then(response => {
        const imageUrl = response.data.message
        const imageBox = document.querySelector('#img-div')
        
        const image = document.createElement('img')
        image.src = imageUrl
        imageBox.appendChild(image)
    })
```

_useAxios.js_

```javascript
// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'

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
```

이게 돌아가기 위한 html은 다음과 같다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="img-div"></div>
    <script src="./userAxios.js"></script>
</body>
</html>
```

