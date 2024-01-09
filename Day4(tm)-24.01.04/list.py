# 75, 80, 70이라는 국어 점수가 있다. 

# 집합 타입(sequence) 
# 값 하나를 저장 : int, float, str, bool
# 값 여러개를 저장 : list, tuple, dictionary, set  -> sequence라고 한다. 

# 원소의 값이 작으면 집합은 비효율적이다.

kor1 = 75
kor2 = 80
kor3 = 90
print(f'국어 점수는 {kor1}, {kor2}, {kor3}다.')

kor= [75, 80, 70]
# kor의 타입 출력 --> list
print(type(kor))

# list는 값이 여러개라는 의미다. 
print(kor)

# 프로그램은 0부터 센다. 
print(kor[0])
print(kor[1])
print(kor[2])
print()

# 사용하는 이유?  변수를 줄이기 위해 list를 사용한다. 그렇기 때문에 다루기가 쉬워진다.


# 조건문, 반복문 
# kor 리스트의 원소를 '하나씩' 꺼내서 item에 담는다.
# 그래서 sequence라고 한다.
for item in kor : 
    print(item)


# 리스트와 튜플의 차이? 리스트는 변경가능하고, 튜플은 변경 불가능 (삭제도 변경이다. )
리스트 = ["사과", "귤", "수박"]
튜플 = ("사과", "귤", "수박")
# CRUD
# Create Read Update Delete
# 변경할 수 있다는 CUD다.

# 그래서 튜플은 읽기만 가능하다. 가볍고 속도가 빠르다. 보통 사용자 값을 가져올때 사용한다. 

# 문제
# 리스트, 튜플 print하세요
# for 담을 변수이름  in sequence이름
for item in 리스트 : 
    print(item)
print()
for item in 튜플 : 
    print(item)

