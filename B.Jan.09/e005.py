# 함수를 정의했으면 다른 파일에서도 가져올 수 있다
import e004
from e004 import hello  # 이거 안하면 e004.hello()라고 해야하고 이거 해주면 그냥 hello()만해도 됨
from e004 import hello, python  # 이렇게 여러개 import할 수 있다.

hello()

# e004에 파이썬이라고 출력하는 함수를 정의하고 e005.py에서 출력
e004.python()
python()


# 함수는 동시에 실행되지 않는다.(한번에 하나씩 실행)
def message():
    print("A")
    print("B")


message()
print("C")
message()

# 병렬 프로그래밍 - 함수를 동시에 실행하는 것
# 코드가 순서대로 동작하는게 기본이지만 서버랑 통신하는 코드는 거의 다 병렬로 돌아감
# 그래서 순서를 잘 맞춰줘야 함


########################
