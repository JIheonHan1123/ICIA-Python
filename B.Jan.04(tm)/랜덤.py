# module(아주 작은 함수) : vscode의 확장프로그램 비슷, 남의 코드를 가져와 기능 확장. 작은 것을 의미한다. (함수 하나) < library < framework(기능 + 사용법)
# 라이브러리는 module의 확장이다.
# 라이브러리는 기능들이다. (내가 가져와서 찾아 써야한다. ) 또한 라이브러리는 설치해야한다.
# import는 다른 프로그래밍에서 작성한 코드를 불러올 때 사용한다.

""" react.js 와 vue(자바스크립트).js
    라이브러리      framework
     6~7개   반복문   <v-for>하나만 있음
     융통성있음     그런거 없음(정해져있음)
"""

# 실수가 나온다. 1보다 작은 실수가 나온다.
import random
print(random.random())

# 앞에 있는 랜덤은 모듈, 뒤에 있는 랜덤은 함수
# 모듈 안에 들어있다.

# print(int(random.random())) 이렇게 하면 0만 나온다.

# 1보다 작은 실수
a = random.random()

# range() 값을 생성한다.
# 예) for i in range(5) -> 0 1 2 3 4

# 10보다 작은 정수
for i in range(5):
    b = int(random.random() * 10)
    print(b)


# 0부터 4까지 5개가 생성된다.
print("")
# 0~10사이의 랜덤 정수 출력
c = int(random.random()*11)
print(c)


p = int((random.random()*10) + 1)
# 1 ~ 10사이의 랜덤 정수 출력

# 10을 곱하면 0~9까지 출력이 된다. 여기다 1을 더해주면 된다.
# 10을 곱하면 1.xxx~ 9.xxxx만 나온다. 그렇게 되면 10이 나오지 않는다. 그래서 11을 곱해서 10을 만드는 것이다.
# 왜 11을 곱하는 거지?
