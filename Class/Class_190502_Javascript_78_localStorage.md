# Javascript 7 & 8강 Vue js로 Todo 앱 만들기

2019-05-02

- localStorage 활용하기

_todo.html_

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Todo App</title>
</head>
<body>
    <div id="app">
        <h1>{{ header }}</h1>
        <p v-once> data 안의 data : {{ msg | capitalize }} </p>
        <p>{{ reverseMsg }}</p>
        <p> 함수 실행의 결과 : {{ hello() }} </p>
        <!-- <img :src="imageSource" width="200" height="200" >
        <a :href="insta">오바마</a> -->
        <input @keyup.enter="addInput" v-model="userInput">
        <button @click="addInput">todo 추가</button> <!--addInput() 혹은 인자 없으면 그냥 addInput만 써도 된다.-->
        <ul>
            <li v-for="(todo, index) in todos">
                <span>{{ (index + 1) * 10}} : {{ todo }}</span>
            </li>
        </ul>
        <p>{{ userInput }}</p>
        <!-- <p>{{ todos }}</p> -->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    // 원하는 형태
    // localStorage = {
    //  'vue-app': []
    // }
    const STORAGE_KEY = 'vue-app'
    const todoStorage = {
        fetch: function() {
            const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
            return data
        },
        save: function(todos) {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
        }
    }
    // todoStorage.save()
    // todoStorage.fetch() // localStorage 데이터를 리턴

    let app = new Vue({
        el: '#app',
        data: {
            header: 'Todo App',
            msg: 'hello',
            userInput: '',
            todos: todoStorage.fetch(),
            imageSource: 'http://catory.kr/files/attach/images/138/009/007/1aa6aaff9f7e241f17a09f077d631206.jpg',
            insta:'https://www.instagram.com/barackobama/'
        },
        methods: {
            hello: function(){
                // this.msg = 'happy hacking'
                return this.msg
            },
            addInput: function(){
                this.todos.push(this.userInput)
                todoStorage.save(this.todos)
                this.clearInput()
            },
            clearInput: function(){
                 // input을 클리어하기
                 this.userInput = ''
             }
        },
        filters: {
            // reverseJoin: function(val) {
            //     return val.reverse().join(' ')
            // },
            capitalize: function(val) {
                if (!val) return ''
                val = val.toString()
                return val.charAt(0).toUpperCase() + val.slice(1)
            }
        },
        computed: {
            reverseMsg: function() {
                return this.msg.split('').reverse().join('')
            }
        },

        // 데이터가 변경되는 것을 지켜보고, 변경시 할 일을 정의
        watch: {
            todos: {
                handler: function() {
                    console.log('todos 변경 됐어요!')
                }
            }
        }
    })
    </script>
</body>
</html>
```



- radio 박스를 사용하여 원하는 이미지 출력하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <style>
      img {
        width: 100px;
    </style>
</head>
<body>
    <div id="main">
        <input type="radio" id="dog" v-model="picked" value="야옹">
        <label for="dog">댕댕이</label>
        <br />
        <input type="radio" id="cat" v-model="picked" value="때껄룩">
        <label for="cat">고양이</label>
        <br /> 
        <span>{{ picked }}</span>
        <br />
        <img v-bind:src="image" />  
    </div>
    <script>
        const dogAndCat = new Vue({
            el:'#main',
            data: {
                picked: '',
                image: '',
            },
            // data의 값을 보고 있다가 data의 값이 바뀌면 특정 함수를 실행
            watch:{
              // TODO: radio 버튼이 눌리면 해당 동물 이미지가 나오도록 하세요!
              picked: function(newPicked){
                if (newPicked==="야옹"){
                  this.getDogImage()
                } else {
                  this.getCatImage()
                }
              }
            },
            methods: {
                getDogImage: function(){
                    const URL = 'https://dog.ceo/api/breeds/image/random'
                    axios.get(URL)
                        .then(response=>{
                            const imageUrl = response.data.message
                            console.log(imageUrl)
                            this.image = imageUrl
                          })
                },
                getCatImage: function(){
                    const URL = 'https://api.thecatapi.com/v1/images/search'
                    axios.get(URL)
                        .then(response=>{
                            const imageUrl = response.data[0].url
                            console.log(imageUrl)
                            this.image = imageUrl
                            })
                }
            }
        })
    </script>
</body>
</html>
```

