# Computational_Thinking

### 대우조건

| p q  | p -> q | ~q  ~p | ~q -> ~p |
| ---- | ------ | ------ | -------- |
| T T  | T      | F F    | T        |
| T F  | F      | T F    | F        |
| F T  | T      | F T    | T        |
| F F  | T      | T T    | T        |



~ : 반대되는 reverse

v : 논리 합 (OR) 

^ : 논리 곱 (AND)

-> : 전제 ~ 라면



p -> q : 기본

q - > p : 역(converse)

~p -> ~q : 이(inverse)

~q -> ~p : 대우(contraposition)

![1569808361013](assets/1569808361013.png) 



Trivial Proof: ∀x,P(x)→Q(x)를증명하려는데, Q(x)가항상참인경우

​	전제의 뒷부분이 참이면 항상 참이 된다.

Vacuous Proof: ∀x,P(x)→Q(x)를증명하려는데, P(x)가항상거짓인경우

​	전제의 앞이 거짓이면 항상 참이 된다.



![Computuonal thinking_00(assets/Computuonal thinking_00(1)-1569832240083.jpg)](../../Downloads/Gmail/Computuonal thinking_00(1).jpg)

![Computuonal thinking_01(assets/Computuonal thinking_01(1)-1569832262568.jpg)](../../Downloads/Gmail/Computuonal thinking_01(1).jpg)

![Computuonal thinking_02(assets/Computuonal thinking_02(1)-1569832262568.jpg)](../../Downloads/Gmail/Computuonal thinking_02(1).jpg)

![Computuonal thinking_04(assets/Computuonal thinking_04(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_04(1).jpg)![Computuonal thinking_03(assets/Computuonal thinking_03(2)-1569832262568.jpg)](../../Downloads/Gmail/Computuonal thinking_03(2).jpg)

![Computuonal thinking_05(assets/Computuonal thinking_05(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_05(1).jpg)

![Computuonal thinking_06(assets/Computuonal thinking_06(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_06(1).jpg)

![Computuonal thinking_07(assets/Computuonal thinking_07(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_07(1).jpg)

![Computuonal thinking_08(assets/Computuonal thinking_08(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_08(1).jpg)

![Computuonal thinking_09(assets/Computuonal thinking_09(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_09(1).jpg)

![Computuonal thinking_10(assets/Computuonal thinking_10(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_10(1).jpg

![Computuonal thinking_11(assets/Computuonal thinking_11(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_11(1).jpg)

![Computuonal thinking_12(assets/Computuonal thinking_12(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_12(1).jpg)

![Computuonal thinking_13(assets/Computuonal thinking_13(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_13(1).jpg)

![Computuonal thinking_14(assets/Computuonal thinking_14(1)-1569832276977.jpg)](../../Downloads/Gmail/Computuonal thinking_14(1).jpg)

![Computuonal thinking_15(assets/Computuonal thinking_15(1)-1569832276978.jpg)](../../Downloads/Gmail/Computuonal thinking_15(1).jpg)

![1569832337831](assets/1569832337831.png)



모든 칸이 감염되기 위해서는 대각선이 모두 감염되어야 한다.

1칸이 감염되어있으면 1칸만 감염

2x2면 대각선 2개가 감염 되어있으면 2^2 감염

3x3 면 대각선 3개가 감염 되어있으면 3^2 감염

