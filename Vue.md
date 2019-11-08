# Vue

### localStorage

`localStorage.setItem('test', "456456")` : 내부 저장소에 있는 값이라면 수정

`localStorage.setItem('test2', "123123")`: 없다면 추가

`JSON.stringify()`: json 형태로 바꿔주는 함수





### 출력하는 방법

```html
<span>{{status}}</span>
<span v-text="status"></span>
<span v-html="tag"></span>
```

`v-html`은 태그를 그대로 반환해주고 싶을 때 사용



```html
<span v-if="false">안녕하세요</span>
<span v-show="false">안녕하세요</span>
```

`v-show`는 `style="display: none;"` 이 추가되고 `v-if `는 주석 처리 된다. 





### Componenet

#### template: 보여줄 html 문서

#### data: 필요한 데이터를 전달하기위한 데이터용 함수공간

#### methods: 필요한 메소드를 사용하기위한 메소드공간

#### props : 부모가 자식한테 데이터를 넘겨주는 변수 저장용 리스트

```html
Vue.component('todo-card',{
      template: `
        <div>
          <h1>{{title}}</h1>
          <h2>{{content}}</h2>
        </div>
      `,
      data: function(){
        return {

        }
      },
      methods: {
        
      },
      props: {
        title: {
          type: String,
          required: true,
          validator: function(input){
            if (input.length < 5){ return false}
            return true
          },
        },
        content: {}
      }
    })
```





## WebPack

`npm` : node pakage manager (pip 와 비슷)

`npm install vue` : 사용자와 개발자 모두에게 필요할 경우 명령어 추가 없이 입력

`npm install webpack-cli -D` : `devDependencies`에 생성되며 개발자만 필요한 도구



#### App.vue 구조

```vue
<template>
  <div>
    <h1>여기는 최상위입니다.</h1>
    <!-- 등록된 컴포넌트를 사용한다. -->
    <todo-list category="싸피"></todo-list>
    <todo-list category="쇼핑"></todo-list>
    <TodoList category="취업"/>
  </div>
</template>


<script>
// 1. 컴포넌트를 가져온다.
import TodoList from './components/TodoList.vue'
export default {
  // 2. 가져온 컴포넌트를 등록한다.
  components: {
    TodoList,
  }
}
</script>

<style>
  .todo-list {
    display: inline-block;
    width: 33%;
  }
</style>
```



#### TodoList.vue 구조 (컴포넌트)

```vue
<template>
  <div class="todo-list">
    <h1>{{category}}</h1>
    <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
    <button v-on:click="addTodo">+</button>
    <li v-for="todo in todos" v-bind:key="todo.id">
    <span>{{ todo.content }}</span>
    <button v-on:click="removeTodo(todo.id)">x</button>
    </li>
  </div>
</template>

<script>
export default {
  props: ['category'],
    data: function(){
    return {
        todos: [],
        newTodo: ''
    }
  },
  methods: {
    addTodo: function(e) {
      if (this.newTodo.length != 0) {
      this.todos.push({
          id: Date.now(),
          content: this.newTodo,
          completed: false,
      })
      this.newTodo = ''
      }
    },
    removeTodo: function(todoID) {
      this.todos = this.todos.filter(todo => {
      return todo.id !== todoID
      })
    }
  },
}
</script>

<style>

</style>
```



#### main.js 구조

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  render: h => h(App)
}).$mount('#app')
// 예전에 쓰던 코드
// const app = new Vue({
//   el: '#app'
// })
```



#### webpack.config.js

```javascript
const path = require('path')
//from path import path
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    mode: 'development',
    entry: {
        app: path.join(__dirname, 'src', 'main.js')
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: ['vue-style-loader', 'css-loader']
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    output: {
        filename: 'app.js',
        path: path.join(__dirname, 'dist')
    },
}
```





### Vue-Cli

`npm install -g @vue/cli` : 기본적인 구조를 잡아주는 vue-cli를 설치하는 명령어

`vue create my-project`: 프로젝트 생성!



## 디렉터리 구조

```
- dist         # 빌드 결과물, yarn build 전까지 없음
- node_modules # yarn 또는 npm으로 설치한 의존성
- public       # 공용으로 접근 가능한 파일이 위치함
- src          # 애플리케이션 소스코드
- test         # 테스트코드
.gitignore
package.json
```



#### 컴포너트 정보를 넘겨주는 방법

##### GetImage.vue

```vue
<template>
  <button v-on:click="onAnimalImage()">{{btnName}}</button>
</template>

<script>
export default {
  props: {
    btnName: String,
  },
  data: function(){
    return {
      
    }
  },
  methods: {
    onAnimalImage: function(){
      this.$emit('getAnimalImage', this.btnName)
    }
  }
}
</script>

<style>

</style>
```



#### App.vue

```vue
<template>
  <div id="app">
    <GetImage btnName="멍멍" @getAnimalImage="getImage"/>  
    <GetImage btnName="야옹" @getAnimalImage="getImage"/>
    <hr>
    <img v-bind:src="animalUrl" alt="">
  </div>
</template>

<script>
import GetImage from './components/GetImage'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    GetImage
  },
  methods: {
    getImage: function(name){

      if (name==="멍멍"){
        const DOG_URL = 'https://dog.ceo/api/breeds/image/random'
        axios.get(DOG_URL)
          .then((response)=>{
            console.log(response)
            this.animalUrl = response.data.message
          })
        .catch((error)=>{console.log(error)})

      } else {


        const CAT_IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
        axios.get(CAT_IMAGE_URL)
          .then((response)=>{
            console.log(response.data[0].url)
            this.animalUrl = response.data[0].url
          })
          .catch((error)=>{console.log(error)})

      }
    }
  },
  data: function(){
    return {
      animalUrl: ''
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

자식요소인 `GetImage.vue`에서  메소드로 `this.$emit('getAnimalImage', this.btnName)` 를 활용해서 `getAnimalImage`를 넘겨주고 부모의 `template` 에서 부모의 메서드와 연결시켜주고 전달해주는 값이 있다면 인자로 받아올 수 있다. `getImage: function(name)` 여기서는 `this.btnName`이 `name`으로 받아졌다.

이후는 `axios`를 활용해서 api에서 값을 불러와서 해결