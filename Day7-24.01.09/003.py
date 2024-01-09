numbers = [1, 3, 5, 7]

num = 7
# 그 숫자가 numbers에 있는지(True, False) 출력
# print(num in numbers)

''' 
이렇게 짜면 True는 그냥 True하고 끝인데 False가 여러번 나옴
if-else로 짜면 안된다.

for item in numbers:
    if item == num:
        print(True)
    else:
        print(False)

찾았다 = 한번만 찾으면 성공
실패 = numbers의 모든 값에 대해서 못 찾아야 실패
=> 성공과 실패의 조건이 다름 => 그래서 if-else가 아니다.
'''

# => 변수를 하나 만든다

isFind = False
for item in numbers:
    if item == num:
        print(True)
        isFind = True
if isFind == False:
    print(False)

# git 배웠지롱