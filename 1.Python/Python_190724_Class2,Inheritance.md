# Python_190724_Class2,Inheritance

## 클래스 변수 / 인스턴스 변수

### 클래스 변수

- 클래스의 속성입니다.

- 클래스 선언 블록 최상단에 위치합니다.

- `Class.class_variable` 과 같이 접근/할당합니다.

  ```python
    class TestClass:
        class_variable = '클래스변수'
        ...
  
    TestClass.class_variable  # '클래스변수'
    TestClass.class_variable = 'class variable'
    TestClass.class_variable  # 'class variable'
  
    tc = TestClass()
    tc.class_variable  # 인스턴스 => 클래스 => 전역 순서로 네임스페이스를 탐색하기 때문에, 접근하게 됩니다.
  ```

### 인스턴스 변수

- 인스턴스의 속성입니다.

- 메서드 정의에서 `self.instance_variable` 로 접근/할당합니다.

- 인스턴스가 생성된 이후 `instance.instance_variable` 로 접근/할당합니다.

  ```python
    class TestClass:
        def __init__(self, arg1, arg2):
            self.instance_var1 = arg1
            self.instance_var2 = arg2
  
        def status(self):
            return self.instance_var1, self.instance_var2   
  
    tc = TestClass(1, 2)
    tc.instance_var1  # 1
    tc.instance_var2  # 2
    tc.status()  # (1, 2)
  ```



## 인스턴스 메서드 / 클래스 메서드 / 스태틱(정적) 메서드

### 인스턴스 메서드

- 인스턴스가 사용할 메서드 입니다.

- **정의 위에 어떠한 데코레이터도 없으면, 자동으로 인스턴스 메서드가 됩니다.**

- **첫 번째 인자로 self 를 받도록 정의합니다. 이 때, 자동으로 인스턴스 객체가 self 가 됩니다.**

  ```python
    class MyClass:
        def instance_method_name(self, arg1, arg2, ...):
            ...
  
    my_instance = MyClass()
    my_instance.instance_method_name(.., ..)  # 자동으로 첫 번째 인자로 인스턴스(my_instance)가 들어갑니다.
  ```

### 클래스 메서드

- 클래스가 사용할 메서드 입니다.

- **정의 위에 @classmethod 데코레이터를 사용합니다.**

- **첫 번째 인자로 cls 를 받도록 정의합니다. 이 때, 자동으로 클래스 객체가 cls 가 됩니다.**

  ```python
    class MyClass:
        @classmethod
        def class_method_name(cls, arg1, arg2, ...):
            ...
  
    MyClass.class_method_name(.., ..)  # 자동으로 첫 번째 인자로 클래스(MyClass)가 들어갑니다.
  ```

### 스태틱(정적) 메서드

- 클래스가 사용할 메서드 입니다.

- **정의 위에 @staticmethod 데코레이터를 사용합니다.**

- **인자 정의는 자유롭게 합니다. 어떠한 인자도 자동으로 넘어가지 않습니다.**

  ```python
    class MyClass:
        @staticmethod
        def static_method_name(arg1, arg2, ...):
            ...
  
    MyClass.static_method_name(.., ..)  # 아무일도 자동으로 일어나지 않습니다.
  ```



# 상속

## 기초

- 클래스에서 가장 큰 특징은 '상속' 기능을 가지고 있다는 것이다.
- 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드재사용성이 높아집니다.

```python
class DerivedClassName(BaseClassName):
    code block
```



```python
class Poketmon:
    def __init__(self, name):
        self.name = name
        self.level = 5
        self.hp = self.level*20
        self.exp = 0
        self.a_value = self.level*2
        
class Fire(Poketmon):
    def __init__(self, name):
        super().__init__(name)     

        
class Pirie(Fire):
    def __init__(self, name):
        super().__init__(name)
        self.spesis = '파이리'
        self.nextspesis = '리자드'
        self.bark()        
```

위와 같이 메소드에서 특정인자를 지정하게 하고 그 메소드를 계속해서 불러내는 것으로 자신의 변수들을 자손에게 물려줄 수 있다. 당연하지만 메소드는 기본적으로 넘어가서 `self.bark()` 와 같이 자식이 불러서 사용할 수 있다.

