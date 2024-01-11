# 나이를 입력받아 성년여부를 리턴하는 함수
'''
def adult_check(age: int):
    if age >= 18:
        print("성년입니다.")
    else:
        print("미성년입니다.")

adult_check(25)
'''
# 위 함수처럼 만들면 바람직하지 않은 함수
# 함수는 결과를 리턴한다. -> 출력할거면 따로 출력
# 리턴하도록 만드는게 바람직하다

'''
def adult_check(age: int):
    if age >= 18:
        return "성년"
    else:
        return "미성년"


age = 24
if adult_check(age) == "성년":  
    print("당신은 출입가능합니다")
'''
# 문자열 가급적이면 피하는게 좋음(오타) => bool


def adult_check(age: int):
    if age >= 18:
        return True  # True면 성인임을 알 수 있게
    else:
        return False


age = 24
if adult_check(age) == True:
    print("당신은 출입가능합니다")
