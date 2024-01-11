# 조건문
'''
a = 10
if a > 5:
    print('if가 참이면 동작')
    print('5보다 큽니다')
    print('들여쓰기 필수')
print('if문과 관계없는 문장')
'''

'''
money = 5000
if money >= 4500:
    print('떡볶이')
    print('햎피햎피햎피')
else:
    print('ㅠㅠㅠㅠ')
print('집도착')
'''

# 점수를 입력 받아 70점 이상이면 합격, 아니면 불합격 출력
# 출력이 끝나면 "수고하셨습니다 출력"
'''
score = int(input('점수입력>> '))
if score >= 70:
    print('합격')
else:
    print('불합격')
print('수고하셨습니다')
'''

# kor=75, eng=80
# 평균이 70점 이상이면 합격, 아니면 불합격 출력
kor, eng = 75, 80
avg = (kor+eng)/2

if avg >= 70:
    print('합격')
else:
    print('불합격')

'''
kor, eng = 75, 80
kor, eng = eng, kor
이런 것도 가능
'''

