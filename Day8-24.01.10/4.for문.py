# for문

# hello를 for를 이용해 3번 출력하시오
'''
for x in (1, 2, 3):
    print('hello')
'''
# 이렇게 하면 (1,2,3)이 아무 의미가 없음
# 그리고 3번 반복이라 괜찮지만 이게 반복횟수가 커지면 문제가 됨
# range로 범위를 생성해줄 수 있다. (idx처럼 0부터 시작)
# range(3) = 0 ,1 ,2 (0부터 3개)
# range(1,6) ="1부터" "6전(5)"까지
'''
for x in range(3):
    print(x)
'''

# ex1) for를 이용해서 0~10까지 출력
'''
for x in range(11):
    print(x)
'''

# ex2) for를 이용해서 0~10 사이의 짝수 출력
'''
for x in range(11):
    if x % 2 == 0:
        print(x)
'''

# ex3) 1부터 5까지의 합계 출력 => 15나와야 함
# 코드 전개하기 전에 생각을 하자
# step1) for가 필요한가? -> O
# step2) if가 필요한가? -> X
result = 0
for i in range(1, 6):
    result = result + i
print(result)
