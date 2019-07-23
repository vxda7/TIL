

# Python_190723_Class

# OOP with python

## 시작하기전에

<wikipedia - 객체지향 프로그래밍>

> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.
>
> 명령형 프로그래밍인 절차지향 프로그래밍에서 발전된 형태를 나타내며, 기본 구성요소는 다음과 같다.

- 클래스(Class)
  - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다
  - 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.

- 인스턴스(instance)
  - 클래스의 인스턴스/객체(실제로 메모리상에 할당된 것)이다.
  - 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.
  - 객체의 행위는 클래스에 정의된 행위에 대한 정의(메서드)를 공유함으로써 메모리를 경제적으로 사용한다.

- 속성(attribute)
  - 클래스/인스턴스 가 가지고 있는 속성(값)

- 메서드(Method)
  - 클래스/인스턴스 가 할 수 있는 행위(함수)





# 클래스 및 인스턴스



## 클래스 정의하기 (클래스 객체 생성하기)

```python
class ClassName:
```

- 선언과 동시에 클래스 객체가 생성됨.
- 또한, 선언된 공간은 지역 스코프로 사용된다.
- 정의된 어트리뷰트 중 변수는 멤버 변수로 불리운다.
- 정의된 함수(`def`)는 메서드로 불리운다.





## 용어 정리

```python
class Person:                     #=> 클래스 정의(선언) : 클래스 객체 생성
    name = 'unknown'              #=> 멤버 변수(data attribute)
    def greeting(self):           #=> 멤버 메서드(메서드)
        return f'{self.name}' 
richard = Person()      # 인스턴스 객체 생성
tim = Person()          # 인스턴스 객체 생성
tim.name                # 데이터 어트리뷰트 호출
tim.greeting()          # 메서드 호출
```



## 클래스-인스턴스간의 이름공간

- 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다.
- 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.
- 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.
- 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 => 클래스 순으로 탐색을 한다.



## 생성자 / 소멸자

- 생성자는 인스턴스 객체가 생성될 때 호출되는 함수이며, 소멸자는 객체가 소멸되는 과정에서 호출되는 함수입니다.

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
__someting__
```

위의 형식처럼 양쪽에 언더스코어가 있는 메서드를 `스페셜 메서드` 혹은 `매직 메서드`라고 불립니다.





## 포켓몬 구현하기

> 피카츄를 클래스-인스턴스로 구현해 봅시다. 게임을 만든다면 아래와 같이 먼저 기획을 하고 코드로 구현하게 됩니다. 우선 아래와 같이 구현해 보고, 추가로 본인이 원하는 대로 구현 및 수정해 봅시다.

모든 피카츄는 다음과 같은 속성을 갖습니다.

- `name`: 이름

- level

  : 레벨

  - 레벨은 시작할 때 모두 5 입니다.

- hp

  : 체력

  - 체력은 `level` * 20 입니다.

- exp

  : 경험치

  - 상대방을 쓰러뜨리면 상대방 `level` * 15 를 획득합니다.
  - 경험치는 `level` * 100 이 되면, 레벨이 하나 올라가고 0부터 추가 됩니다.

모든 피카츄는 다음과 같은 행동(메서드)을 할 수 있습니다.

- `bark()`: 울기. `'pikachu'` 를 출력합니다.
- `body_attack()`: 몸통박치기. 상대방의 hp 를 내 `level` * 5 만큼 차감합니다.
- `thousond_volt()`: 십만볼트. 상대방의 hp 를 내 `level` * 7 만큼 차감합니다.



```python
# 아래에 코드를 작성해주세요.
class Pikachu:
    def __init__(self, name):
        self.name = name
        self.level = 5
        self.hp = self.level*20
        self.exp = 0
        self.spesis = '피카츄'
        print("피카피카")
    
    def status(self):
        print(f"이름 : {self.name}")
        print(f"레벨 : {self.level}")
        print(f"HP : {self.hp}")
        print(f"EXP : {self.exp}")
        print(f"종족 : {self.spesis}")
        
    def bark(self):
        print('pikachu')
        
    def levelup(self):
        self.exp-=self.level*100
        self.level+=1
        print(f'{self.name}의 레벨업! {self.level}이 되었다.')
        if self.level>=10:
            self.revolution()
        
    def revolution(self):
        print(f'{self.name}의 상태가 이상하다!')
        self.spesis = '라이츄'
        print(f'{self.name}은 {self.spesis}로 진화했다!')
        
    def body_attack(self,enemy):
        if type(enemy) == Pikachu:
            enemy.hp-=self.level*5
            print(f'{self.name}의 몸통박치기!')
            print(f"{enemy.name}은 {self.level*5}의 피해를 입었다. {self.name}의 hp:{self.hp} {enemy.name}의 hp:{enemy.hp}")
            if enemy.hp <= 0:
                print(f'{self.name}이 이겼다!')
                print(f'{enemy.level*15}exp를 획득했다!')
                self.exp+=enemy.level*15
                if self.exp >= self.level*100:
                    self.levelup()  
                enemy.hp=enemy.level*20
                self.hp=self.level*20
        
    def thousond_volt(self,enemy):
        if type(enemy) == Pikachu:
            enemy.hp-=self.level*7
            print(f'{self.name}의 천만볼트!!!')
            print(f"{enemy.name}은 {self.level*7}의 피해를 입었다. {self.name}의 hp:{self.hp} {enemy.name}의 hp:{enemy.hp}")
            if enemy.hp <= 0:
                print(f'{self.name}이 이겼다!')
                print(f'{enemy.level*15}exp를 획득했다!')
                self.exp+=enemy.level*15
                if self.exp >= self.level*100:
                    self.levelup()
                enemy.hp=enemy.level*20
                self.hp=self.level*20
```





```
31.400000000000002
```

위와 같은 숫자가 나오는 이유는 int형과 float형의 연산에서 잔여물이 나오는 것으로 추측된다.



## Data Structure

## `map()`, `zip()`, `filter()`

### `map(function, iterable)`

- Iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려줍니다.
- 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
- return은 map_object 형태로 됩니다.



### `zip(*iterables)`

- 복수 iterable한 것들을 모아준다.
- 결과는 튜플의 모음으로 구성된 zip object를 반환한다.



### `filter(function, iterable)`

- iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.