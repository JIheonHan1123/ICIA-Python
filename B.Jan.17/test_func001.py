# from func001 import sample1, sample2
import func001 as f

# 테스트하는 함수를 작성
# 이렇게 함수를 테스트 하는 것을 unit test(단위 테스트)라고 한다.
# 테스트하는 함수는 pytest로 실행이 가능
# 항상 tset_와 assert로 시작. assert 안쓰면 무조건 초록색나와서 의미가 없음
'''
def test_sample1():
    assert sample1()==10
'''

# 이렇게 테스트할 코드 만들고
# 터미널에 => pytest 파일명 => 치면 테스트 결과 나옴
# ex) pytest test_func001.py
'''
def test_round():
    assert round(2.5)==3
'''

# return이 없는 함수는 테스트가 안된다!
'''
def test_sample2():
    assert sample2()
'''

# def test_is_adult():
#     assert is_adult(20) is True
#     assert is_adult(18) is True
#     assert is_adult(14) is False


# def test_get_fees():
#     assert get_fees(25) == 3000
#     assert get_fees(64) == 3000
#     assert get_fees(30) == 3000
#     assert get_fees(20) == 0
#     assert get_fees(65) == 0


def test_get_fees2():
    assert f.get_fees2(9) == 27000
    assert f.get_fees2(10) == 24000
    assert f.get_fees2(100) == 240000
