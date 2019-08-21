# Agorithm 190821 Queue

## Queue

**큐**(queue)는 [컴퓨터](https://ko.wikipedia.org/wiki/컴퓨터)의 기본적인 [자료 구조](https://ko.wikipedia.org/wiki/자료_구조)의 한가지로, 먼저 집어 넣은 [데이터](https://ko.wikipedia.org/wiki/데이터)가 먼저 나오는 [FIFO](https://ko.wikipedia.org/wiki/FIFO) (First In First Out)구조로 저장하는 형식을 말한다. 영어 단어 queue는 표를 사러 일렬로 늘어선 사람들로 이루어진 줄을 말하기도 하며, 먼저 줄을 선 사람이 먼저 나갈 수 있는 상황을 연상하면 된다.

나중에 집어 넣은 데이터가 먼저 나오는 [스택](https://ko.wikipedia.org/wiki/스택)과는 반대되는 개념이다.

[프린터](https://ko.wikipedia.org/wiki/프린터)의 [출력](https://ko.wikipedia.org/wiki/출력) 처리나 [윈도 시스템](https://ko.wikipedia.org/wiki/윈도_시스템)의 메시지 처리기, [프로세스 관리](https://ko.wikipedia.org/wiki/프로세스_관리) 등 데이터가 [입력](https://ko.wikipedia.org/wiki/입력)된 시간 순서대로 처리해야 할 필요가 있는 상황에 이용된다.

### 선형[[편집](https://ko.wikipedia.org/w/index.php?title=큐_(자료_구조)&action=edit&section=3)]

막대 모양으로 된 큐이다. 크기가 제한되어 있고 빈 공간을 사용하려면 모든 자료를 꺼내거나 자료를 한 칸씩 옮겨야 한다는 단점이 있다.

다음은 선형 큐의 작동 방식이다.

DATA : A B C D E

|      |
| ---- |
|      |
|      |
| A    |

|      |
| ---- |
|      |
| B    |
| A    |

|      |
| ---- |
| C    |
| B    |
| A    |

|      |
| ---- |
| C    |
| B    |
|      |

| D    |
| ---- |
| C    |
| B    |
|      |

| D    |
| ---- |
| C    |
|      |
|      |



### 환형 큐[[편집](https://ko.wikipedia.org/w/index.php?title=큐_(자료_구조)&action=edit&section=4)]

선형 큐의 문제점(배열로 큐를 선언할시 큐의 삭제와 생성이 계속 일어났을때, 마지막 배열에 도달후 실제로는 데이터공간이 남아있지만 오버플로우가 발생)을 보완한 것이 환형 큐이다. front가 큐의 끝에 닿으면 큐의 맨 앞으로 자료를 보내어 원형으로 연결 하는 방식이다. 
원형 큐라고도 한다.
DATA : A B C D E

|      |
| ---- |
|      |
|      |
| A    |

|      |
| ---- |
|      |
| B    |
| A    |

|      |
| ---- |
| C    |
| B    |
| A    |

| D    |
| ---- |
| C    |
| B    |
| A    |

| D    |
| ---- |
| C    |
| B    |
|      |

| D    |
| ---- |
| C    |
| B    |
| E    |