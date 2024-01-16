# 제어문 for, while

# 주민번호를 입력받아 성별을 출력
"""
jumin = "971012-1035112"
if jumin[7] in ["1","3","5"] :
    print("남자입니다.")
elif jumin[7] in ["2","4","6"]  :
    print("여자입니다.")
else : 
    print("잘못된 문자입니다.")
"""
# 문자열인지 정확하게 봐야한다. 문자열로 자르면 문자로 비교해야한다.
# in만 쓰면 이 값이 포함되어 있는지 물어보는 것으로 사용된다.
# if jumin[7] in ("1", "2", "3") 앞에있는 변수가 1,3,5가 포함되어있는지 물어보는 것이다.

# 주민번호를 입력받아 태어난 년도를 계산해 나이 출력
# 90년대면 1,2 - 2000년대면 3,4
this_year = 2024

jumin = "011203-3411111"
if jumin[7] in ["1", "2"]:
    birthday = '19' + jumin[0:2]
    birthday = int(birthday)
    print(birthday)
    print(this_year-(birthday))
elif jumin[7] in ["3", "4"]:
    birthday = '20' + jumin[0:2]
    birthday = int(birthday)
    print(this_year-(birthday))
else:
    print("잘못된 값이다.")

# 97을 자른 다음 "19" + "97" 또는 "20" + "97"
