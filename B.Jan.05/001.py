# list, tuple, set
# 반복 for while
# 함수 dictionary


# html, css


# 3주차부터 오라클 할거임
# flask 웹서버로 할 일 관리

# 3~4주차
# crud 작업
# 조별로 간단한 게시판 만들기


# 이러고 자바 갈거

# 사용자가 회원가입 하려고 다양한 데이터를 넘길 때
# 튜플로 받거나 딕셔너리로 받는다 --> 리스트로 받지 않는다.
# 왜?Why? -


# ------------------------
# slicing - 글자를 자르는 것 (리스트나 튜플에서도 슬라이싱할 수 있음)
lang = 'python'
print(lang[0])  # p
print(lang[5])  # n
print('a' in lang)  # a라는 글자가 lang안에 있는지 알고 싶을 때
print('p' in lang)

# 뒤에서부터 slicing할 수도 있다
print(lang[-1])  # n
# 뒤에서부터 세는 경우
# aaa.hwp, dfadsr.hwp 이런 파일이 있다 했을 때 확장자만 확인하려면 뒤에서부터 세는게 편함
# 앞에서부터 시작하는게 0이기 때문에 뒤에서 부터 시작하는건 -1로 시작한다.90

# 부분적으로 자를 때
string = '123456789'
# 문자열[ 시작위치 : 끝위치+1 ]
print(string[1:3])  # 23

# 문자열 [ 시작위치 : 끝위치+1 : 간격 ]
print(string[1:])  # 23456789 (생략하면 끝까지)
print(string[1::5])  # 27

# ex) 위 string에서 짝수만 출력
print(string[1::2])  # 2468

# ex)
jumin = '961011-1021023'
gender = jumin[7]
# 남자인지 여자인지 출력
if gender == '1':
    print('남자')
else:
    print('여자')

# '둘 중의 하나 if문'을 한줄로 -> 삼항연산자: 항이 3개인거 (자바할때 자세히 설명할거임)
# elif는 못 쓴다
# tip! 복잡한 조건 삼항연산은 쓰지말자 --> 코드가 난해해짐(스파게티 코드)
# cf) 스파게티코드(), 외계인코드(규칙 안지키고 희한하게 짠 코드)
print("남자" if gender == '1' else "여자")

# gender가 1또는3또는5면 남자, 아니면 여자
print("남자" if gender == '1' or gender == '3' or gender == '5' else '여자')
print("남자" if gender in ('1', '3', '5') else '여자')
