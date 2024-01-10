# control: 실행 순서를 바꾼다.
# control에는 조건과 반복이 있다.

# 조건: 결과가 이럴수도 있고 저럴수도 있다.
# 반복: 말그대로 반복


''''''
# 조건
# Day2 조건 참고
# if-else

# score가 홀수인지 짝수인지 출력해라 (2의 배수)
# cf) 어떤 수가 n의 배수인지 확인하는 법 -> n으로 나누었을 때 나머지가 0
score = 75
if score % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 다중조건
# 점수가 90이상이면 우수, 70이상이면 합격, 미만이면 재시험
score = 75
if score >= 90:
    print('우수')
elif score >= 70:
    print('합격')
else:
    print('재시험')

# 주의사항
# else는 짬통이 아니다. 자신 없으면 elif 써라
# else로 빠지는 조건을 정확히 알 때만 else 사용


''''''
# 반복 for, while

