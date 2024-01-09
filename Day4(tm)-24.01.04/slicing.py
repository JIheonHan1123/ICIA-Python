# slicing
리스트 = [10,20,30,40,50]
# 리스트[시작 인덱스 : 끝 인덱스 +1]
# 끝 인덱스 + 1은 그 앞까지 출력해준다.
print(리스트[0:2])
print(리스트[1:4])

# slicing은 문자열도 가능 (문자열은 list가 아니지만 자르는 것은 가능하다.)
string = "0123456"
print(string[1:3])

print(string[2:5])

# 어디부터 끝까지
print(string[3:])

# 간격지정
print(string[3::2])

# string에서 홀수 문자를 출력
print(string[1::2])
# 2칸꺼를 가지고 온다

print(string[2::2])

