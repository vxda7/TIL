# JavaScript

#### var, const, let

`var`: 둘다 가능

`const`: 선언과 동시에 할당해줘야함 한번씩만 가능

`let`: 선언만 한번 할당은 여러번 가능



### typeof

`NaN, infinity, 숫자`



#### 조건 / 반복

`if, else if, for, for of, while`



#### `==`, `===`

내용비교와 타입과 함께 비교



### Array

`.length` 리스트의 길이 반영

`.push('a')` 리스트의 가장 뒤에 넣기

`.pop()` 리스트의 가장 뒤에서 빼오기

`.indexOf('a')` 처음 찾은 요소의 index

`.join('')` 요소로 묶어서 default는 , 문자열반환

`shift, unshift` 앞에서  빼고 넣기



###  Object

```javascript
const bookShop = {
	books,
	comics,
	magazines,
}
```



### function

`const p = function(){return 'hello'}()` : 함수 선언과 동시에 괄호를 실행하면 함수가 실행된다. 여기서 p는 'hello'로 저장되었다.

`const p = function(){return 'hello'}`: 이렇게 하면 함수가 p에 저장된다.



### axios

```javascript
axios.get('요청 url')
	.then((response)=>{
		console.log(response)
	})
	.catch((error)=>{
		console.log(error)
	})
```

`api`에 요청을 보내서 원하는 결과를 받아오는 `http` 통신용 `javascript`라이브러리 이다.

